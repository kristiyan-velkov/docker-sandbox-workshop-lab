(function () {
  const configUrl = new URL("config.json", document.baseURI).toString();

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function renderAuthor(author) {
    if (!author?.name) return "";

    const authorLinks = Array.isArray(author.links)
      ? author.links
      : author.url
        ? [{ label: "LinkedIn", url: author.url }]
        : [];
    const linksHtml = authorLinks
      .map(
        (link) =>
          `<a href="${escapeHtml(link.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(
            link.label,
          )}</a>`,
      )
      .join("");

    return `
      <div class="catalog-promo-author">
        <p class="catalog-promo-author-name">${escapeHtml(author.name)}</p>
        ${
          author.title
            ? `<p class="catalog-promo-author-title">${escapeHtml(author.title)}</p>`
            : ""
        }
        ${
          linksHtml
            ? `<div class="catalog-promo-socials">${linksHtml}</div>`
            : ""
        }
      </div>
    `;
  }

  function renderPromo(presentation) {
    const section = document.createElement("section");
    section.className = "catalog-promo";
    section.innerHTML = `
      <div class="catalog-promo-head">
        <span class="catalog-promo-icon" aria-hidden="true">
          <span class="material-symbols-outlined">slideshow</span>
        </span>
        <div class="catalog-promo-copy">
          <h2 class="catalog-promo-title">${escapeHtml(presentation.title)}</h2>
          <p class="catalog-promo-desc">${escapeHtml(presentation.description)}</p>
          ${renderAuthor(presentation.author)}
        </div>
      </div>
      <a class="catalog-promo-action" href="${escapeHtml(
        presentation.url,
      )}" target="_blank" rel="noopener noreferrer">
        ${escapeHtml(presentation.buttonLabel || "Open presentation")}
        <span class="material-symbols-outlined" aria-hidden="true">open_in_new</span>
      </a>
    `;
    return section;
  }

  function enhanceCatalogCards(github) {
    if (!github?.repo) return;

    document.querySelectorAll(".catalog-card").forEach((card) => {
      if (card.querySelector(".catalog-chip-github")) return;

      const labPath = card.getAttribute("href") || "";
      const labId = labPath.split("/").filter(Boolean).pop();
      if (!labId) return;

      const githubUrl = `${github.repo.replace(/\/+$/, "")}/${labId}`;
      const meta = card.querySelector(".catalog-card-meta");
      const chip = document.createElement("a");
      chip.className = "catalog-chip catalog-chip-github";
      chip.href = githubUrl;
      chip.target = "_blank";
      chip.rel = "noopener noreferrer";
      chip.innerHTML = `<span class="material-symbols-outlined">code</span>${escapeHtml(
        github.label || "GitHub lab",
      )}`;
      chip.addEventListener("click", (event) => event.stopPropagation());

      if (meta) {
        meta.prepend(chip);
      } else {
        const body = card.querySelector(".catalog-card-body");
        if (!body) return;
        const metaRow = document.createElement("span");
        metaRow.className = "catalog-card-meta";
        metaRow.appendChild(chip);
        body.appendChild(metaRow);
      }
    });
  }

  fetch(configUrl)
    .then((response) => (response.ok ? response.json() : null))
    .then((config) => {
      const root = document.getElementById("root");
      if (!root) return;

      const observer = new MutationObserver(() => {
        const grid = document.querySelector(".catalog-grid");
        if (!grid) return;

        const presentation = config?.presentation;
        if (
          presentation?.url &&
          presentation?.title &&
          !document.querySelector(".catalog-promo")
        ) {
          grid.parentElement.insertBefore(renderPromo(presentation), grid);
        }

        enhanceCatalogCards(config?.github);
      });

      observer.observe(root, { childList: true, subtree: true });
    })
    .catch(() => {});
})();

(function () {
  const HOME = "~";
  let cwd = HOME;

  function normalizePath(path) {
    if (!path || path === HOME) return HOME;
    const cleaned = path.replace(/\/+$/, "");
    return cleaned || HOME;
  }

  function resolveCd(current, target) {
    const t = target.trim();
    if (!t || t === HOME) return HOME;
    if (t === ".") return current;
    if (t === "..") {
      if (current === HOME) return HOME;
      const parts = current.split("/").filter(Boolean);
      parts.pop();
      return parts.length ? parts.join("/") : HOME;
    }
    if (t.startsWith("/")) return normalizePath(t.slice(1));
    if (t.includes("/")) {
      return current === HOME
        ? normalizePath(t)
        : normalizePath(`${current}/${t}`);
    }
    return current === HOME ? t : `${current}/${t}`;
  }

  function formatPrompt(path) {
    return path === HOME ? "~$ " : `${path}$ `;
  }

  function stripShellPrompt(line) {
    const idx = line.indexOf("$");
    if (idx === -1) return line.trim();
    return line.slice(idx + 1).trim();
  }

  function replayCwdFromTranscript() {
    let next = HOME;
    document.querySelectorAll(".term-line.term-input").forEach((el) => {
      const command = stripShellPrompt(el.textContent || "");
      if (!command.startsWith("cd")) return;
      const arg = command.slice(2).trim();
      next = resolveCd(next, arg);
    });
    cwd = next;
  }

  function isShellPromptElement(el) {
    const text = (el.textContent || "").trim();
    if (!text) return true;
    if (text.startsWith(">")) return false;
    if (text.includes("Enter secret")) return false;
    if (text.includes("Your Docker Hub username")) return false;
    if (text.includes("AI:")) return false;
    return text === "$" || text.endsWith("$");
  }

  function applyPrompts() {
    const prompt = formatPrompt(cwd);
    document.querySelectorAll(".term-prompt").forEach((el) => {
      if (!isShellPromptElement(el)) return;
      if (el.textContent !== prompt) el.textContent = prompt;
    });
  }

  function tick() {
    replayCwdFromTranscript();
    applyPrompts();
    requestAnimationFrame(tick);
  }

  function bootTerminalCwd() {
    replayCwdFromTranscript();
    applyPrompts();
    requestAnimationFrame(tick);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bootTerminalCwd);
  } else {
    bootTerminalCwd();
  }
})();

(function () {
  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  const MD_LINK =
    /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g;
  const BARE_URL = /https?:\/\/[^\s<>"')]+/g;

  function linkifyPlainText(text) {
    return escapeHtml(text).replace(BARE_URL, (url) => {
      return `<a class="term-link" href="${escapeHtml(
        url,
      )}" target="_blank" rel="noopener noreferrer">${escapeHtml(url)}</a>`;
    });
  }

  function linkifyText(text) {
    MD_LINK.lastIndex = 0;
    const hasMarkdownLink = MD_LINK.test(text);
    MD_LINK.lastIndex = 0;
    if (!hasMarkdownLink) {
      return linkifyPlainText(text);
    }

    let html = "";
    let lastIndex = 0;
    let match;

    while ((match = MD_LINK.exec(text)) !== null) {
      html += linkifyPlainText(text.slice(lastIndex, match.index));
      html += `<a class="term-link" href="${escapeHtml(
        match[2],
      )}" target="_blank" rel="noopener noreferrer">${escapeHtml(match[1])}</a>`;
      lastIndex = MD_LINK.lastIndex;
    }

    html += linkifyPlainText(text.slice(lastIndex));
    return html;
  }

  function linkifyTerminalLines() {
    document.querySelectorAll(".mock-term .term-line").forEach((el) => {
      if (el.closest(".term-inputrow")) return;
      if (el.querySelector("a.term-link")) return;

      const text = el.textContent;
      if (!text || !/(https?:\/\/|\[[^\]]+\]\(https?:\/\/)/.test(text)) return;

      el.innerHTML = linkifyText(text);
    });
  }

  function bootTerminalLinks() {
    linkifyTerminalLines();
    requestAnimationFrame(function tick() {
      linkifyTerminalLines();
      requestAnimationFrame(tick);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bootTerminalLinks);
  } else {
    bootTerminalLinks();
  }
})();

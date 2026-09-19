#!/usr/bin/env python3
"""Inject workshop landing-page assets into Simspace index.html."""

from __future__ import annotations

import sys
from pathlib import Path


def patch(index_path: Path) -> None:
    html = index_path.read_text()
    css = '<link rel="stylesheet" href="./workshop-catalog-promo.css">'
    js = '<script defer src="./workshop-catalog-promo.js"></script>'

    if "workshop-catalog-promo.css" not in html:
        html = html.replace("</head>", f"    {css}\n  </head>")
    if "workshop-catalog-promo.js" not in html:
        html = html.replace("</body>", f"    {js}\n  </body>")

    index_path.write_text(html)


if __name__ == "__main__":
    patch(Path(sys.argv[1]))

#!/usr/bin/env bash
# Assemble a static Simspace site from the runtime image + this repo's labs,
# then apply workshop-specific landing-page overlays (presentation callout).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SITE_DIR="${1:-$ROOT/site}"
LABS_DIR="${2:-$ROOT/labs}"
RUNTIME_IMAGE="${RUNTIME_IMAGE:-dockersamples/simspace:latest}"
AUTHORING_IMAGE="${AUTHORING_IMAGE:-dockersamples/simspace-authoring:latest}"

for required in \
  "$ROOT/public/config.json" \
  "$ROOT/public/workshop-catalog-promo.css" \
  "$ROOT/public/workshop-catalog-promo.js" \
  "$ROOT/scripts/patch-index-html.py"; do
  if [[ ! -f "$required" ]]; then
    echo "Missing deploy asset: $required" >&2
    exit 1
  fi
done

rm -rf "$SITE_DIR"
mkdir -p "$SITE_DIR"

cid="$(docker create "$RUNTIME_IMAGE")"
trap 'docker rm -f "$cid" >/dev/null 2>&1 || true' EXIT
docker cp "$cid":/usr/share/nginx/html/. "$SITE_DIR/"
docker rm -f "$cid" >/dev/null
trap - EXIT

rm -rf "$SITE_DIR/labs" "$SITE_DIR/labs.json"
mkdir -p "$SITE_DIR/labs"
cp -R "$LABS_DIR/." "$SITE_DIR/labs/"

docker run --rm \
  -v "$ROOT:/work" \
  "$AUTHORING_IMAGE" \
  npm run generate-catalog -- "/work/$(basename "$LABS_DIR")" "/work/site/labs.json"

cp "$ROOT/public/config.json" "$SITE_DIR/config.json"
cp "$ROOT/public/workshop-catalog-promo.css" "$SITE_DIR/workshop-catalog-promo.css"
cp "$ROOT/public/workshop-catalog-promo.js" "$SITE_DIR/workshop-catalog-promo.js"
python3 "$ROOT/scripts/patch-index-html.py" "$SITE_DIR/index.html"

echo "Assembled site at $SITE_DIR"

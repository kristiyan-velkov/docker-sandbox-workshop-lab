#!/bin/bash
# Launch the live Labspace track (real sbx terminal).
set -e

TTYD_PORT=8085
COMPOSE_FILE=".labspace/compose.override.yaml"

RED='\033[0;31m'; GREEN='\033[0;32m'; NC='\033[0m'
info() { echo -e "${GREEN}==>${NC} $*"; }
error() { echo -e "${RED}ERROR:${NC} $*"; exit 1; }

if ! command -v ttyd &>/dev/null; then
  error "ttyd not found. Install: brew install ttyd"
fi

if ! command -v sbx &>/dev/null; then
  error "sbx not found. Install: brew install docker/tap/sbx"
fi

sbx daemon start 2>/dev/null || true
info "sbx version: $(sbx version 2>/dev/null)"

export CONTENT_PATH="${CONTENT_PATH:-$(pwd)}"
info "CONTENT_PATH=$CONTENT_PATH"

if [ ! -f "$COMPOSE_FILE" ]; then
  error "$COMPOSE_FILE not found — run from repo root"
fi

lsof -ti tcp:$TTYD_PORT | xargs kill -9 2>/dev/null || true
sleep 1

info "Starting terminal on port $TTYD_PORT..."
ttyd -p $TTYD_PORT --writable --max-clients 4 zsh &
TTYD_PID=$!
sleep 1

info "Starting Labspace..."
docker compose -f oci://dockersamples/labspace -f "$COMPOSE_FILE" up &
COMPOSE_PID=$!

echo ""
echo "==========================================="
echo " Labspace ready at http://localhost:3030"
echo " Terminal → real sbx on your machine"
echo "==========================================="
echo ""

cleanup() {
  info "Stopping..."
  kill $TTYD_PID 2>/dev/null || true
  docker compose -f oci://dockersamples/labspace -f "$COMPOSE_FILE" down 2>/dev/null || true
}
trap cleanup EXIT
wait $COMPOSE_PID

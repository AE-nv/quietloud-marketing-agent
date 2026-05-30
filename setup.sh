#!/usr/bin/env bash
set -e

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_DIR="$ROOT/quietloud-campaign-intelligence"

echo "==> QuietLoud Campaign Intelligence — setup"
echo "    Root: $ROOT"

# --- Validate plugin MCP config ---
echo "==> Using plugin MCP config at $PLUGIN_DIR/.mcp.json"
test -f "$PLUGIN_DIR/.mcp.json"

# --- Register marketplace and install plugin ---
echo "==> Registering marketplace..."
codex plugin marketplace add "$ROOT" 2>/dev/null || echo "    (marketplace already registered)"

echo "==> Installing plugin..."
codex plugin add quietloud-campaign-intelligence@personal 2>/dev/null || \
  echo "    (plugin already installed)"

echo ""
echo "Done. Open a new Codex session and say: 'Start a QuietLoud campaign workflow'"

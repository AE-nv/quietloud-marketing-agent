#!/usr/bin/env bash
set -e

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_DIR="$ROOT/quietloud-campaign-intelligence"

echo "==> QuietLoud Campaign Intelligence — setup"
echo "    Root: $ROOT"

# --- Find Python 3.10+ ---
# Prefer Codex bundled Python, fall back to system
CODEX_PY="$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
if [ -x "$CODEX_PY" ]; then
  PY="$CODEX_PY"
  echo "==> Using Codex bundled Python: $PY"
else
  for candidate in python3.13 python3.12 python3.11 python3.10; do
    if command -v "$candidate" &>/dev/null; then
      PY=$(command -v "$candidate")
      break
    fi
  done
  if [ -z "$PY" ]; then
    echo "ERROR: Python 3.10+ required. Install via pyenv or Homebrew."
    exit 1
  fi
  echo "==> Using system Python: $PY ($($PY --version))"
fi

# --- Virtualenv ---
if [ ! -d "$ROOT/.venv" ]; then
  echo "==> Creating venv..."
  "$PY" -m venv "$ROOT/.venv"
fi
VENV_PY="$ROOT/.venv/bin/python"
echo "==> Installing dependencies..."
"$VENV_PY" -m pip install -q --upgrade pip
"$VENV_PY" -m pip install -q -r "$ROOT/requirements.txt"
echo "    OK"

# --- Regenerate .mcp.json with correct absolute paths ---
echo "==> Writing plugin .mcp.json..."
cat > "$PLUGIN_DIR/.mcp.json" <<EOF
{
  "mcpServers": {
    "quietloud-signal-extraction":   { "command": "$VENV_PY", "args": ["$ROOT/mcp-servers/signal-extraction/server.py"] },
    "quietloud-audience-reasoning":  { "command": "$VENV_PY", "args": ["$ROOT/mcp-servers/audience-reasoning/server.py"] },
    "quietloud-customer-profile":    { "command": "$VENV_PY", "args": ["$ROOT/mcp-servers/customer-profile/server.py"] },
    "quietloud-outreach-method":     { "command": "$VENV_PY", "args": ["$ROOT/mcp-servers/outreach-method/server.py"] },
    "quietloud-executing-agent":     { "command": "$VENV_PY", "args": ["$ROOT/mcp-servers/executing-agent/server.py"] },
    "quietloud-message-formatting":  { "command": "$VENV_PY", "args": ["$ROOT/mcp-servers/message-formatting/server.py"] },
    "quietloud-graphical-pipeline":  { "command": "$VENV_PY", "args": ["$ROOT/mcp-servers/graphical-pipeline/server.py"] },
    "quietloud-representation":      { "command": "$VENV_PY", "args": ["$ROOT/mcp-servers/representation/server.py"] }
  }
}
EOF

# --- Register MCP servers with Codex ---
echo "==> Registering MCP servers with Codex..."
for server in signal-extraction audience-reasoning customer-profile outreach-method executing-agent message-formatting graphical-pipeline representation; do
  codex mcp add "quietloud-$server" -- "$VENV_PY" "$ROOT/mcp-servers/$server/server.py" 2>/dev/null || \
    echo "    (quietloud-$server already registered, skipping)"
done

# --- Register marketplace and install plugin ---
echo "==> Registering marketplace..."
codex plugin marketplace add "$ROOT" 2>/dev/null || echo "    (marketplace already registered)"

echo "==> Installing plugin..."
codex plugin add quietloud-campaign-intelligence@personal 2>/dev/null || \
  echo "    (plugin already installed)"

echo ""
echo "Done. Open a new Codex session and say: 'Start a QuietLoud campaign workflow'"
echo ""
echo "Don't forget to set your API key:"
echo "  export ANTHROPIC_API_KEY=<your-key>"

#!/bin/bash
# GCF Hermes Dashboard — Start

HERMES_PY="$HOME/.hermes/hermes-agent/venv/bin/python3"
cd "$(dirname "$0")"

echo "🚀 Starting GCF Hermes Dashboard..."
echo "   Open: http://localhost:4096"
echo "   Stop: Ctrl+C"
echo ""

exec $HERMES_PY server.py

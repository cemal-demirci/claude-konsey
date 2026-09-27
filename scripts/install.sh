#!/usr/bin/env bash
# Eklenti sistemi kullanmadan, skill'i doğrudan ~/.claude/skills/konsey altına kurar.
# Kullanım: scripts/install.sh [--tema klasik|kurtlar] [--mod hizli|standart|derin]
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${CLAUDE_HOME:-$HOME/.claude}"
TEMA=""; MOD=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --tema) TEMA="$2"; shift 2 ;;
    --mod) MOD="$2"; shift 2 ;;
    *) echo "bilinmeyen seçenek: $1" >&2; exit 2 ;;
  esac
done

python3 "$ROOT/scripts/validate.py"

mkdir -p "$DEST/skills" "$DEST/agents"
rm -rf "$DEST/skills/konsey"
cp -R "$ROOT/skills/konsey" "$DEST/skills/konsey"
cp "$ROOT/agents/konsey-uyesi.md" "$DEST/agents/konsey-uyesi.md"
echo "✔ skill: $DEST/skills/konsey"
echo "✔ alt-ajan: $DEST/agents/konsey-uyesi.md"

if [[ -n "$TEMA$MOD" ]]; then
  python3 - "$DEST/konsey.json" "$TEMA" "$MOD" <<'PY'
import json, sys, os
path, tema, mod = sys.argv[1:4]
cfg = json.load(open(path)) if os.path.exists(path) else {}
if tema: cfg["tema"] = tema
if mod: cfg["mod"] = mod
json.dump(cfg, open(path, "w"), ensure_ascii=False, indent=2)
print(f"✔ ayarlar: {path} → {cfg}")
PY
fi
echo "Yeni bir Claude Code oturumu açıp \"konseyi topla: …\" yazın."

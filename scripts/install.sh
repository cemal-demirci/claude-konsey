#!/usr/bin/env bash
# Eklenti sistemi kullanmadan Konsey'i doğrudan ~/.claude altına kurar:
#   skills/konsey/            skill
#   agents/konsey-uyesi.md    üye alt-ajanı
#   commands/konsey-topla.md  /konsey-topla komutu (eklentideki /konsey:topla'nın karşılığı)
#   konsey.json               --tema / --mod verilirse varsayılan ayarlar
# Kullanım: scripts/install.sh [--tema klasik|kurtlar] [--mod hizli|standart|derin]
# Hedef klasör CLAUDE_HOME ile değiştirilebilir (varsayılan: ~/.claude).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${CLAUDE_HOME:-$HOME/.claude}"
TEMA=""; MOD=""

usage() { sed -n '2,8p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; }

while [[ $# -gt 0 ]]; do
  case "$1" in
    --tema) [[ $# -ge 2 ]] || { echo "--tema bir değer ister" >&2; exit 2; }; TEMA="$2"; shift 2 ;;
    --mod)  [[ $# -ge 2 ]] || { echo "--mod bir değer ister" >&2; exit 2; }; MOD="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "bilinmeyen seçenek: $1" >&2; usage >&2; exit 2 ;;
  esac
done

if [[ -n "$TEMA" && ! -f "$ROOT/skills/konsey/themes/$TEMA.md" ]]; then
  echo "bilinmeyen tema: $TEMA (var olanlar: $(cd "$ROOT/skills/konsey/themes" && ls *.md | sed 's/\.md$//' | tr '\n' ' '))" >&2
  exit 2
fi
case "$MOD" in ""|hizli|standart|derin) ;; *) echo "bilinmeyen mod: $MOD (hizli | standart | derin)" >&2; exit 2 ;; esac

python3 "$ROOT/scripts/validate.py"

mkdir -p "$DEST/skills" "$DEST/agents" "$DEST/commands"
rm -rf "$DEST/skills/konsey"
cp -R "$ROOT/skills/konsey" "$DEST/skills/konsey"
cp "$ROOT/agents/konsey-uyesi.md" "$DEST/agents/konsey-uyesi.md"
cp "$ROOT/commands/topla.md" "$DEST/commands/konsey-topla.md"
echo "✔ skill: $DEST/skills/konsey"
echo "✔ alt-ajan: $DEST/agents/konsey-uyesi.md"
echo "✔ komut: $DEST/commands/konsey-topla.md (/konsey-topla)"

if [[ -n "$TEMA$MOD" ]]; then
  python3 - "$DEST/konsey.json" "$TEMA" "$MOD" <<'PY'
import json, sys, os
path, tema, mod = sys.argv[1:4]
cfg = {}
if os.path.exists(path):
    try:
        with open(path, encoding="utf-8") as f:
            cfg = json.load(f)
    except json.JSONDecodeError:
        print(f"! {path} bozuktu, yeniden yazılıyor", file=sys.stderr)
if tema: cfg["tema"] = tema
if mod: cfg["mod"] = mod
with open(path, "w", encoding="utf-8") as f:
    json.dump(cfg, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"✔ ayarlar: {path} → {cfg}")
PY
fi
echo "Yeni bir Claude Code oturumu açıp \"konseyi topla: …\" yazın."

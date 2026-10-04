#!/usr/bin/env bash
# Çalışma klasörüne proje düzeyinde bir Konsey ayar dosyası koyar (gerçek ~/.claude'a dokunmaz).
set -euo pipefail
mkdir -p .claude
printf '{ "tema": "klasik", "mod": "hizli" }\n' > .claude/konsey.json

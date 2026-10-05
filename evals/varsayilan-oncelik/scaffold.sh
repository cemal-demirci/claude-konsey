#!/usr/bin/env bash
# Eval çalışma klasörü <sandbox>/home/cwd, ajanın HOME'u <sandbox>/home'dur. Kullanıcı düzeyi ayarı bu geçici
# HOME'a, proje ayarını çalışma klasörüne yazar. Gerçek ~/.claude'a asla dokunmaz: klasör düzeni beklenen gibi
# değilse hiçbir şey yazmadan çıkar.
set -euo pipefail
CWD="$(pwd -P)"
[[ "$(basename "$CWD")" == "cwd" && "$(basename "$(dirname "$CWD")")" == "home" ]] || {
  echo "beklenmeyen çalışma klasörü: $CWD" >&2; exit 1; }
SANDBOX_HOME="$(dirname "$CWD")"
REAL_HOME="$(python3 -c 'import os, pwd; print(pwd.getpwuid(os.getuid()).pw_dir)')"
[[ "$SANDBOX_HOME" != "$REAL_HOME" ]] || { echo "geçici HOME gerçek HOME ile aynı: $REAL_HOME" >&2; exit 1; }
mkdir -p .claude "$SANDBOX_HOME/.claude"
printf '{ "tema": "klasik" }\n' > .claude/konsey.json
printf '{ "tema": "kurtlar", "mod": "hizli" }\n' > "$SANDBOX_HOME/.claude/konsey.json"

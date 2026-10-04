#!/usr/bin/env python3
"""Konsey eklentisinin yapısını denetler (CI'da ve yerelde çalışır; bağımlılık yok).

Denetlenenler:
  - SKILL.md ön bilgisi (name, description, açıklama uzunluğu)
  - SKILL.md ve protokollerde adı geçen her dosyanın var olması
  - Her temanın 7 rol + başkan satırını ve banner başlığını eksiksiz tanımlaması
  - Üye alt-ajanının yalnızca salt-okunur araçlara sahip olması
  - plugin.json ile marketplace.json sürümlerinin tutarlı olması
  - Her eval senaryosunun bir istemi ve en az bir değerlendiricisi olması
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "konsey"
ROLES = ["Eleştirmen", "Stratejist", "Analist", "Vizyoner", "Mühendis", "Filozof", "Hümanist", "Başkan"]
READ_ONLY_TOOLS = {"Read", "Grep", "Glob"}
MAX_DESCRIPTION = 1024

errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        err(f"{path.relative_to(ROOT)}: ön bilgi (---) yok")
        return {}
    out, key = {}, None
    for line in m.group(1).splitlines():
        kv = re.match(r"^([\w-]+):\s*(.*)$", line)
        if kv:
            key = kv.group(1)
            out[key] = kv.group(2).strip()
        elif key and line.startswith("  "):
            out[key] = (out[key].rstrip(">").strip() + " " + line.strip()).strip()
    return out


def check_skill() -> None:
    fm = frontmatter(SKILL / "SKILL.md")
    if fm.get("name") != "konsey":
        err("SKILL.md: name 'konsey' olmalı")
    desc = fm.get("description", "")
    if not desc:
        err("SKILL.md: description boş")
    elif len(desc) > MAX_DESCRIPTION:
        err(f"SKILL.md: description {len(desc)} karakter (en fazla {MAX_DESCRIPTION})")

    # Adı geçen tüm yerel dosyalar var mı?
    for md in [SKILL / "SKILL.md", *sorted((SKILL / "protocol").glob("*.md")), *sorted((SKILL / "templates").glob("*.md"))]:
        for ref in re.findall(r"`((?:personas|themes|templates|protocol)/[\w./<>-]+\.md)`", md.read_text(encoding="utf-8")):
            if "<" in ref:
                continue  # themes/<tema>.md gibi kalıplar
            if not (SKILL / ref).exists():
                err(f"{md.relative_to(ROOT)}: adı geçen dosya yok: {ref}")

    personas = sorted(p.stem for p in (SKILL / "personas").glob("*.md"))
    expected = sorted(["adversary", "strategist", "scientist", "visionary", "engineer", "philosopher", "humanist"])
    if personas != expected:
        err(f"personas/: beklenen {expected}, bulunan {personas}")


def theme_rows(text: str) -> dict[str, list[str]]:
    rows = {}
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and cells[0] in ROLES:
            rows[cells[0]] = cells[:4]
    return rows


def check_inline_themes() -> None:
    """SKILL.md'ye gömülü temalar themes/*.md ile birebir aynı olmalı (skill başka dosya okumadan çalışır)."""
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    sections = re.split(r"^### Tema: (\w+)\s*$", text, flags=re.M)
    inline = {sections[i]: sections[i + 1] for i in range(1, len(sections) - 1, 2)}
    if "klasik" not in inline:
        err("SKILL.md: '### Tema: klasik' gömülü değil")
    for name, body in inline.items():
        body = body.split("\n## ")[0]
        f = SKILL / "themes" / f"{name}.md"
        if not f.exists():
            err(f"SKILL.md: gömülü tema '{name}' için themes/{name}.md yok")
            continue
        if theme_rows(body) != theme_rows(f.read_text(encoding="utf-8")):
            err(f"SKILL.md: gömülü '{name}' teması themes/{name}.md ile uyuşmuyor")
        banner = re.search(r"^Banner başlığı: `([^`]+)`", body, re.M)
        fbanner = re.search(r"^Banner başlığı: `([^`]+)`", f.read_text(encoding="utf-8"), re.M)
        if not banner or not fbanner or banner.group(1) != fbanner.group(1):
            err(f"SKILL.md: '{name}' banner başlığı themes/{name}.md ile uyuşmuyor")


def check_themes() -> None:
    themes = sorted((SKILL / "themes").glob("*.md"))
    if not themes:
        err("themes/: hiç tema yok")
    for t in themes:
        text = t.read_text(encoding="utf-8")
        rows = {}
        for line in text.splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 4 and cells[0] in ROLES:
                rows[cells[0]] = cells
        for role in ROLES:
            if role not in rows:
                err(f"themes/{t.name}: '{role}' satırı yok")
                continue
            _, name, title, style = rows[role][:4]
            if not name or not title.strip("`") or not style:
                err(f"themes/{t.name}: '{role}' satırında boş hücre var")
        if not re.search(r"^Banner başlığı: `[^`]+`", text, re.M):
            err(f"themes/{t.name}: 'Banner başlığı: `…`' satırı yok")
    names = [t.stem for t in themes]
    if "klasik" not in names:
        err("themes/: varsayılan 'klasik' teması yok")


def check_agent() -> None:
    fm = frontmatter(ROOT / "agents" / "konsey-uyesi.md")
    tools = {x.strip() for x in fm.get("tools", "").split(",") if x.strip()}
    if not tools:
        err("agents/konsey-uyesi.md: tools belirtilmemiş (boş = tüm araçlar)")
    elif not tools <= READ_ONLY_TOOLS:
        err(f"agents/konsey-uyesi.md: salt-okunur olmayan araç: {sorted(tools - READ_ONLY_TOOLS)}")
    for k in ("name", "description"):
        if not fm.get(k):
            err(f"agents/konsey-uyesi.md: {k} yok")


def check_name_collisions() -> None:
    """Aynı adlı komut ve skill çakışır: Skill aracı skill yerine komut metnini yükler."""
    skills = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
    commands = {p.stem for p in (ROOT / "commands").glob("*.md")}
    for name in sorted(skills & commands):
        err(f"commands/{name}.md ile skills/{name}/ aynı adı taşıyor; komutu yeniden adlandırın")


def check_manifests() -> None:
    try:
        plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        err(f".claude-plugin: okunamadı: {e}")
        return
    entry = next((p for p in market.get("plugins", []) if p.get("name") == plugin.get("name")), None)
    if entry is None:
        err("marketplace.json: plugin.json'daki eklenti listede yok")
    elif entry.get("version") != plugin.get("version"):
        err(f"sürüm uyuşmuyor: plugin.json {plugin.get('version')} ≠ marketplace.json {entry.get('version')}")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8") if (ROOT / "CHANGELOG.md").exists() else ""
    if plugin.get("version") and f"## {plugin['version']}" not in changelog:
        err(f"CHANGELOG.md: '## {plugin.get('version')}' başlığı yok")


GRADER_TYPES = {"regex", "tool_order", "tool_used", "file_exists", "llm", "baseline"}


def check_evals() -> None:
    """evals/<senaryo>/ ya prompt.md + graders/*.md ya da case.yaml içermeli."""
    evals = ROOT / "evals"
    if not evals.is_dir():
        err("evals/: klasör yok")
        return
    cases = [d for d in sorted(evals.iterdir()) if d.is_dir() and d.name not in ("results", "mocks")]
    if not cases:
        err("evals/: hiç senaryo yok")
    for d in cases:
        rel = d.relative_to(ROOT)
        case_yaml = d / "case.yaml"
        if case_yaml.exists():
            text = case_yaml.read_text(encoding="utf-8")
            if not re.search(r"^graders:", text, re.M):
                err(f"{rel}/case.yaml: graders yok")
            for t in re.findall(r"^\s+type:\s*(\S+)", text, re.M):
                if t not in GRADER_TYPES:
                    err(f"{rel}/case.yaml: bilinmeyen değerlendirici tipi: {t}")
            m = re.search(r"^\s+scaffold_script:\s*(\S+)", text, re.M)
            if m and not (d / m.group(1)).exists():
                err(f"{rel}/case.yaml: scaffold_script yok: {m.group(1)}")
            continue
        if not (d / "prompt.md").exists():
            err(f"{rel}: prompt.md ya da case.yaml yok")
            continue
        graders = sorted((d / "graders").glob("*.md"))
        if not graders:
            err(f"{rel}: graders/*.md yok")
        for g in graders:
            t = frontmatter(g).get("type")
            if t not in GRADER_TYPES:
                err(f"{g.relative_to(ROOT)}: bilinmeyen ya da eksik type: {t}")


def main() -> int:
    check_skill()
    check_themes()
    check_inline_themes()
    check_agent()
    check_name_collisions()
    check_manifests()
    check_evals()
    if errors:
        print("✘ Konsey denetimi başarısız:")
        for e in dict.fromkeys(errors):
            print(f"  - {e}")
        return 1
    print("✔ Konsey denetimi geçti")
    return 0


if __name__ == "__main__":
    sys.exit(main())

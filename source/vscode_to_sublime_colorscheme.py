"""
Convert a VS Code theme JSON (with include chain) into a Sublime Text
.sublime-color-scheme (modern JSON format), which is the preferred format
in Sublime 3+/4 over legacy .tmTheme.

Handles VS Code's `include` mechanism by recursively flattening the chain.
"""
import json
from pathlib import Path
import sys

# Reuse include flattening + scope helpers from the tmTheme generator
sys.path.insert(0, str(Path(__file__).parent))
from vscode_to_tmtheme import load_theme_dir, to_six, fmt_style


GLOBAL_MAP = [
    ("editor.background",            "background"),
    ("editor.foreground",             "foreground"),
    ("editorCursor.foreground",      "caret"),
    ("editor.selectionBackground",    "selection"),
    ("editor.inactiveSelectionBackground", "selection_inactive"),
    ("editor.selectionHighlightBackground", "highlight"),
    ("editor.findMatchBackground",    "find_highlight"),
    ("editor.findMatchHighlightBackground", "find_highlight_inactive"),
    ("editor.lineHighlightBackground", "line_highlight"),
    ("editorGutter.foreground",       "gutter"),
    ("editorLineNumber.foreground",   "gutter_foreground"),
    ("editorWhitespace.foreground",    "invisibles"),
    ("editorIndentGuide.background",    "guide"),
    ("editorIndentGuide.activeBackground", "active_guide"),
    ("editor.wordHighlightBackground", "brackets_foreground"),
    ("editor.wordHighlightStrongBackground", "brackets_content_foreground"),
]


def sem_to_scope(t):
    sys_path = {
        "keyword": "keyword", "keyword.control": "keyword.control",
        "keyword.operator": "keyword.operator", "keyword.type": "storage.type",
        "type": "entity.name.type", "class": "entity.name.class",
        "interface": "entity.name.interface",
        "function": "entity.name.function", "function.defaultLibrary": "entity.name.function",
        "method": "entity.name.function.method",
        "property": "variable.other.property", "parameter": "variable.parameter",
        "variable": "variable", "variable.defaultLibrary": "variable.language",
        "number": "constant.numeric", "string": "string",
        "boolean": "constant.language.boolean", "constant": "constant.other",
        "macro": "support.function.macro", "comment": "comment",
        "namespace": "entity.name.namespace", "module": "entity.name.module",
    }
    return sys_path.get(t)


def convert(in_path: Path, out_path: Path):
    data = load_theme_dir(in_path)
    colors = data.get("colors", {})
    token_colors = data.get("tokenColors", [])
    sem = data.get("semanticTokenColors", {})

    scheme = {
        "name": data.get("name", "InuProt"),
        "author": "CudtMFrag (InuProt), derived from Human Theme (Tom Hall) and VS Code 2026 Light.",
        "variables": {},
        "globals": {},
        "rules": [],
    }
    for vsc, sb in GLOBAL_MAP:
        if vsc in colors:
            scheme["globals"][sb] = to_six(colors[vsc])

    seen = set()
    for r in token_colors:
        sc = r.get("scope")
        if not sc:
            continue
        key = sc if isinstance(sc, str) else tuple(sc)
        if key in seen:
            continue
        seen.add(key)
        scope_str = sc if isinstance(sc, str) else " ".join(sc)
        st = r.get("settings", {})
        rule = {"scope": scope_str}
        if st.get("foreground"):
            rule["foreground"] = to_six(st["foreground"])
        if st.get("background"):
            rule["background"] = to_six(st["background"])
        fs = fmt_style(st.get("fontStyle"))
        if fs:
            rule["font_style"] = fs
        scheme["rules"].append(rule)

    for st_type, color in sem.items():
        scope = sem_to_scope(st_type)
        if not scope:
            continue
        if isinstance(color, dict):
            fg = color.get("foreground")
            fs = fmt_style(color.get("fontStyle"))
        else:
            fg, fs = color, ""
        if not fg and not fs:
            continue
        rule = {"scope": scope}
        if fg:
            rule["foreground"] = to_six(fg)
        if fs:
            rule["font_style"] = fs
        scheme["rules"].append(rule)

    out_path.write_text(json.dumps(scheme, indent=2, ensure_ascii=False),
                        encoding="utf-8")
    print(f"OK  {in_path.name:18s} -> {out_path.name:30s}  ({len(scheme['rules'])} rules, bg={scheme['globals'].get('background')})")


if __name__ == "__main__":
    base = Path(r"C:/tmp/InuProt")
    jobs = [
        (base / "vscode/themes/inuprot-dark.json",  base / "sublime/InuProt Dark.sublime-color-scheme"),
        (base / "vscode/themes/inuprot-light.json", base / "sublime/InuProt Light.sublime-color-scheme"),
    ]
    for i, o in jobs:
        convert(i, o)
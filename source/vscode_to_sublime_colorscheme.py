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
    ("editorLineNumber.activeForeground", "gutter_foreground_highlight"),
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
        "author": "CudtMFrag (InuProt), derived from Human Theme (Tom Hall) and GitHub Light Colorblind Beta (Primer / GitHub).",
        "variables": {},
        "globals": {},
        "rules": [],
    }
    for vsc, sb in GLOBAL_MAP:
        if vsc in colors:
            scheme["globals"][sb] = to_six(colors[vsc])

    # VS Code applies tokenColors in order: the last setting for a given
    # scope wins. Sublime also uses later-wins, but only when selectors are
    # not duplicated. Expand list scopes into individual selectors and keep
    # the last setting per selector so Sublime matches VS Code exactly.
    final_settings = {}
    for r in token_colors:
        sc = r.get("scope")
        if not sc:
            continue
        selectors = [sc] if isinstance(sc, str) else sc
        st = r.get("settings", {})
        for sel in selectors:
            final_settings[sel] = st

    for sel, st in final_settings.items():
        rule = {"scope": sel}
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
    # C# compatibility: Sublime scopes the `in` in `foreach (var x in y)` as
    # keyword.operator.iteration.in.cs, while VS Code treats it as a plain
    # keyword (same color as int/double). Map it to the keyword color so the
    # two editors agree.
    is_dark = data.get("type") == "dark"
    keyword_color = "#00AA00" if is_dark else "#CF222E"
    scheme["rules"].append({"scope": "keyword.operator.iteration.in.cs", "foreground": to_six(keyword_color)})


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

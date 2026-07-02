"""
Convert InuProt VS Code theme JSONs into Sublime Text / TextMate color schemes
(.tmTheme XML plist).

Handles VS Code's `include` mechanism by recursively merging every linked
theme's `colors` and `tokenColors` (deeper-first so the outermost theme wins),
so the resulting .tmTheme is fully self-contained and works in Sublime Text
(which has no include mechanism).
"""
import json
import uuid
import html
from pathlib import Path


GLOBAL_MAP = [
    ("editor.background",            "background"),
    ("editor.foreground",             "foreground"),
    ("editorCursor.foreground",      "caret"),
    ("editor.selectionBackground",    "selection"),
    ("editor.inactiveSelectionBackground", "selectionInactive"),
    ("editor.selectionHighlightBackground", "highlight"),
    ("editor.findMatchBackground",    "findHighlight"),
    ("editor.findMatchHighlightBackground", "highlightInactive"),
    ("editor.lineHighlightBackground", "lineHighlight"),
    ("editor.wordHighlightBackground", "bracketsForeground"),
    ("editorGutter.foreground",       "gutter"),
    ("editorLineNumber.foreground",   "gutterForeground"),
    ("editorWhitespace.foreground",    "invisibles"),
    ("editorIndentGuide.background",   "guide"),
    ("editorIndentGuide.activeBackground", "activeGuide"),
]

SCOPE_NAMES = {
    "comment": "Comment", "string": "String", "constant.numeric": "Number",
    "constant.language": "Built-in constant", "constant.language.boolean": "Boolean",
    "constant.character": "Character", "constant.character.escape": "Character escape",
    "keyword": "Keyword", "keyword.control": "Control keyword",
    "keyword.control.return": "Return", "keyword.operator": "Operator",
    "keyword.operator.new": "Operator new", "storage.type": "Storage type",
    "storage.modifier": "Storage modifier", "entity.name.function": "Function name",
    "entity.name.type": "Type name", "entity.name.class": "Class name",
    "entity.name.interface": "Interface name", "entity.name.tag": "Tag",
    "entity.other.attribute-name": "Attribute name", "variable": "Variable",
    "variable.parameter": "Parameter", "variable.language": "Special variable",
    "variable.other.constant": "Constant variable", "support.type": "Support type",
    "support.function": "Support function", "support.constant": "Support constant",
    "support.class": "Support class", "support.variable": "Support variable",
    "meta.decorator": "Decorator", "punctuation": "Punctuation",
    "punctuation.separator": "Separator", "punctuation.terminator": "Terminator",
    "punctuation.accessor": "Accessor", "invalid": "Invalid",
    "markup.heading": "Heading", "markup.bold": "Bold markup",
    "markup.italic": "Italic markup", "markup.inserted": "Diff inserted",
    "markup.deleted": "Diff deleted", "markup.changed": "Diff changed",
    "string.regexp": "Regexp",
}

SEM_TO_SCOPE = {
    "keyword": "keyword", "keyword.control": "keyword.control",
    "keyword.operator": "keyword.operator", "keyword.type": "storage.type",
    "type": "entity.name.type", "type.defaultLibrary": "entity.name.type",
    "class": "entity.name.class", "class.defaultLibrary": "entity.name.class",
    "interface": "entity.name.interface", "interface.defaultLibrary": "entity.name.interface",
    "enum": "entity.name.type.enum", "enum.defaultLibrary": "entity.name.type.enum",
    "typeAlias": "entity.name.type.alias", "struct": "entity.name.struct",
    "function": "entity.name.function", "function.defaultLibrary": "entity.name.function",
    "method": "entity.name.function.method", "method.defaultLibrary": "entity.name.function.method",
    "method.readonly": "entity.name.function.method",
    "property": "variable.other.property", "property.readonly": "variable.other.property",
    "property.static": "variable.other.property", "parameter": "variable.parameter",
    "parameter.readonly": "variable.parameter",
    "variable": "variable", "variable.readonly": "variable",
    "variable.defaultLibrary": "variable.language",
    "number": "constant.numeric", "string": "string",
    "boolean": "constant.language.boolean", "constant": "constant.other",
    "macro": "support.function.macro", "comment": "comment",
    "namespace": "entity.name.namespace", "namespace.defaultLibrary": "entity.name.namespace",
    "module": "entity.name.module",
}


def to_six(c):
    s = c.strip().lstrip("#")
    if len(s) == 8: s = s[:6]
    if len(s) == 3: s = "".join(ch*2 for ch in s)
    return f"#{s}".upper()


def esc(s):
    return html.escape(s, quote=True)


def scope_name(scope):
    if isinstance(scope, list): scope = scope[0]
    return SCOPE_NAMES.get(scope, scope)


def fmt_style(fs):
    if not fs: return ""
    return " ".join(p.lower() for p in str(fs).split()
                    if p.lower() in ("bold","italic","underline","strikethrough"))


def load_theme_dir(path: Path):
    """Return dict theme, recursively merging include chain (deepest first).
    Outer theme overrides inner."""
    d = json.load(open(path, encoding="utf-8"))
    inc = d.get("include")
    if inc:
        inc_path = (path.parent / inc.lstrip("./"))
        if inc_path.exists():
            base = load_theme_dir(inc_path)
            # base first, d overrides
            merged_colors = {**base.get("colors", {}), **d.get("colors", {})}
            merged_tokens = list(base.get("tokenColors", [])) + list(d.get("tokenColors", []))
            merged_sem = {**base.get("semanticTokenColors", {}), **d.get("semanticTokenColors", {})}
            d["colors"] = merged_colors
            d["tokenColors"] = merged_tokens
            d["semanticTokenColors"] = merged_sem
    return d


def build_global(colors):
    out = ['    <dict>\n      <key>settings</key>\n      <dict>\n']
    for vsc, tm in GLOBAL_MAP:
        if vsc in colors:
            out.append(f'        <key>{tm}</key>\n        <string>{to_six(colors[vsc])}</string>\n')
    out.append('      </dict>\n    </dict>\n')
    return "".join(out)


def build_rule(scope, settings):
    # TextMate scope selectors use spaces for hierarchical nesting (a inside b)
    # and COMMAS to separate alternative selectors (== OR). VS Code's
    # tokenColors represents alternatives as a list; join with ", " so Sublime
    # / TextMate reads them as alternatives, not nesting.
    scope_str = scope if isinstance(scope, str) else ", ".join(scope)
    out = ['    <dict>\n']
    out.append(f'      <key>name</key><string>{esc(scope_name(scope))}</string>\n')
    out.append(f'      <key>scope</key><string>{esc(scope_str)}</string>\n')
    out.append('      <key>settings</key>\n      <dict>\n')
    if settings.get("foreground"):
        out.append(f'        <key>foreground</key><string>{to_six(settings["foreground"])}</string>\n')
    if settings.get("background"):
        out.append(f'        <key>background</key><string>{to_six(settings["background"])}</string>\n')
    st = fmt_style(settings.get("fontStyle"))
    if st:
        out.append(f'        <key>fontStyle</key><string>{st}</string>\n')
    out.append('      </dict>\n    </dict>\n')
    return "".join(out)


def build_sem_rule(st_type, color):
    scope = SEM_TO_SCOPE.get(st_type)
    if not scope: return ""
    settings = {}
    if isinstance(color, dict):
        if "foreground" in color: settings["foreground"] = color["foreground"]
        if "fontStyle" in color: settings["fontStyle"] = color["fontStyle"]
    else:
        settings["foreground"] = color
    if not settings: return ""
    return build_rule(scope, settings)


def convert(in_path: Path, out_path: Path):
    data = load_theme_dir(in_path)
    name = data.get("name", "InuProt")
    colors = data.get("colors", {})
    token_colors = data.get("tokenColors", [])
    sem = data.get("semanticTokenColors", {})

    parts = []
    parts.append('<?xml version="1.0" encoding="UTF-8"?>\n')
    parts.append('<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" '
                 '"http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n')
    parts.append('<plist version="1.0">\n<dict>\n')
    parts.append(f'  <key>name</key><string>{esc(name)}</string>\n')
    parts.append('  <key>settings</key>\n  <array>\n')
    parts.append(build_global(colors))
    seen = set()
    for r in token_colors:
        sc = r.get("scope")
        if not sc: continue
        key = sc if isinstance(sc, str) else tuple(sc)
        if key in seen: continue
        seen.add(key)
        parts.append(build_rule(sc, r.get("settings", {})))
    for st_type, color in sem.items():
        line = build_sem_rule(st_type, color)
        if line: parts.append(line)
    parts.append('  </array>\n')
    parts.append(f'  <key>uuid</key><string>{str(uuid.uuid4())}</string>\n')
    parts.append('</dict>\n</plist>\n')

    out_path.write_text("".join(parts), encoding="utf-8")
    n_rules = sum(1 for x in parts if "<key>scope</key>" in x)
    print(f"OK  {in_path.name:18s} -> {out_path.name:22s}  ({n_rules} scope rules)")


if __name__ == "__main__":
    base = Path(r"C:/tmp/InuProt")
    jobs = [
        (base / "vscode/themes/inuprot-dark.json",  base / "sublime/InuProt Dark.tmTheme"),
        (base / "vscode/themes/inuprot-light.json", base / "sublime/InuProt Light.tmTheme"),
    ]
    for i, o in jobs:
        convert(i, o)
"""
Generate InuProt theme preview screenshots, fully static (no JS highlighter).

The code sample is hand-annotated with the relevant TextMate scope for each
token, and the colors are pulled directly from InuProt tokenColors. This makes
the render 100% deterministic and independent of network/JS timing, so Edge
headless screenshots are reliable.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(r"C:/tmp/InuProt")
sys.path.insert(0, str(ROOT / "source"))
from vscode_to_tmtheme import load_theme_dir, to_six  # noqa: E402


def html_escape(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;"))


def first_color_for_scope(theme_data, scope_name):
    """Return foreground hex (6-digit) for the first tokenColor rule whose
    scope list contains scope_name; fall back to semantic / editor foreground."""
    for rule in theme_data.get("tokenColors", []):
        sc = rule.get("scope")
        if not sc:
            continue
        scopes = [sc] if isinstance(sc, str) else sc
        for s in scopes:
            # match hierarchical scope like 'keyword.control' against rule scope
            # 'keyword.control.catch' only if rule is more specific - we just do
            # substring-ish hierarchical match: rule scope s should be a prefix
            if s == scope_name or scope_name.startswith(s + "."):
                st = rule.get("settings", {})
                if st.get("foreground"):
                    return to_six(st["foreground"])
    return None


# (token text, TextMate scope) — hand-annotated sample.
# Chosen to show the green-vs-orange contrast this theme is tuned for:
#   keyword (green) / control-flow (orange) / string (orange) / number (orange) / function (green) / type (teal)
SAMPLE = [
    ("# Comment: green keywords vs orange control-flow & strings\n", "comment"),
    ("import", "keyword.import"),
    (" { useState } ", "variable"),
    ("from", "keyword.import"),
    (" \"react\"", "string"),
    (";\n\n", "punctuation"),

    ("export", "keyword.export"),
    (" function ", "storage.type"),
    ("Counter", "entity.name.function"),
    ("() {\n", "punctuation"),

    ("  const", "storage.type"),
    (" [count, setCount] =", "variable"),
    (" useState", "entity.name.function"),
    ("(0)", "constant.numeric"),
    (";\n", "punctuation"),

    ("  const", "storage.type"),
    (" threshold =", "variable"),
    (" 100", "constant.numeric"),
    (";\n\n", "punctuation"),

    ("  if", "keyword.control"),
    (" (count >= threshold) {\n", "punctuation"),

    ("    return <span>", "keyword.control.return"),
    ("Max reached", "string"),
    ("</span>;\n", "punctuation"),

    ("  }\n\n", "punctuation"),

    ("  try", "keyword.control"),
    (" {\n", "punctuation"),

    ("    setCount", "entity.name.function"),
    ("(count + 1)", "constant.numeric"),
    (";\n", "punctuation"),

    ("  } catch", "keyword.control"),
    (" (error) {\n", "variable.parameter"),

    ("    throw new ", "keyword.control"),
    ("Error", "support.class"),
    ("(\"counter failed\")", "string"),
    (";\n", "punctuation"),

    ("  }\n\n", "punctuation"),

    ("  return `count: ${count}`", "string"),
    (";\n", "punctuation"),

    ("}", "punctuation"),
]


def build_rendered_code(theme_data):
    """Produce HTML for SAMPLE with each token wrapped in a colored span."""
    fg = to_six(theme_data["colors"].get("editor.foreground", "#000000"))
    parts = []
    parts.append(f"<code style=\"color: {fg}\">")
    for text, scope in SAMPLE:
        color = first_color_for_scope(theme_data, scope)
        if not color:
            # try a more generic scope (e.g. keyword.control -> keyword)
            parent = scope.split(".")[0]
            color = first_color_for_scope(theme_data, parent) or fg
        escaped = html_escape(text)
        parts.append(f'<span style="color: {color}">{escaped}</span>')
    parts.append("</code>")
    return "".join(parts)


HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>
  body {{
    margin: 0;
    padding: 32px 36px 36px;
    background: {bg};
    color: {fg};
    font-family: "JetBrains Mono", "Cascadia Code", "Fira Code", Consolas, "Courier New", monospace;
    font-size: 15px;
    line-height: 1.65;
    -webkit-font-smoothing: antialiased;
  }}
  pre {{
    margin: 0;
    padding: 0;
    background: transparent;
    white-space: pre;
    tab-size: 2;
  }}
  pre code {{ background: transparent; padding: 0; }}
  .badge {{
    display: inline-block;
    margin-bottom: 18px;
    padding: 5px 12px;
    background: {accent};
    color: {accentfg};
    font-family: -apple-system, "Segoe UI", Roboto, sans-serif;
    font-size: 13px;
    font-weight: 700;
    border-radius: 5px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }}
  .sample-label {{
    margin-top: 6px;
    font-family: -apple-system, "Segoe UI", Roboto, sans-serif;
    font-size: 11px;
    color: {muted};
    opacity: 0.7;
  }}
</style>
</head>
<body>
  <div class="badge">{title}</div>
  <pre>{code}</pre>
  <div class="sample-label">JavaScript — keyword (green) vs control-flow &amp; string &amp; number (orange) contrast</div>
</body>
</html>
"""


MSEDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"


def build_html(theme_path: Path, out_html: Path, title: str, is_dark: bool):
    data = load_theme_dir(theme_path)
    bg = to_six(data["colors"].get("editor.background", "#FFFFFF"))
    fg = to_six(data["colors"].get("editor.foreground", "#000000"))
    code = build_rendered_code(data)
    if is_dark:
        accent, accentfg = "#00AA00", "#000000"
        muted = "#AAAAAA"
    else:
        accent, accentfg = "#2c6e1f", "#FFFFFF"
        muted = "#7a8a78"
    html = HTML_HEAD.format(
        bg=bg, fg=fg, title=title, code=code,
        accent=accent, accentfg=accentfg, muted=muted,
    )
    out_html.write_text(html, encoding="utf-8")
    return bg, fg


def screenshot(html_path: Path, png_path: Path):
    url = "file:///" + str(html_path).replace("\\", "/")
    png_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        MSEDGE,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=2",
        "--window-size=780,620",
        "--default-background-color=00000000",
        "--virtual-time-budget=1500",
        f"--screenshot={png_path}",
        url,
    ]
    print("  -> running edge headless...", end=" ")
    r = subprocess.run(cmd, capture_output=True, timeout=90)
    ok = png_path.exists() and png_path.stat().st_size > 1000
    print("ok" if ok else "FAILED")
    if not ok:
        sys.stderr.write(r.stderr.decode("utf-8", "replace")[:600])
        sys.exit(1)


def main():
    jobs = [
        (ROOT / "vscode/themes/inuprot-dark.json",
         ROOT / "previews/inuprot-dark.html",
         ROOT / "previews/inuprot-dark.png",
         "InuProt Dark", True),
        (ROOT / "vscode/themes/inuprot-light.json",
         ROOT / "previews/inuprot-light.html",
         ROOT / "previews/inuprot-light.png",
         "InuProt Light", False),
    ]
    for theme, html, png, title, is_dark in jobs:
        print(f"=== {title} ===")
        bg, fg = build_html(theme, html, title, is_dark)
        print(f"  bg={bg} fg={fg}")
        screenshot(html, png)
        print(f"  wrote {png.name} ({png.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
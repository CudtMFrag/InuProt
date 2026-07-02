# Third-Party Notices

InuProt is derived from and incorporates material from two MIT-licensed
upstream projects. Both licenses permit modification and redistribution
provided their copyright notices are retained.

This file reproduces the upstream copyright notices for the portions of code
and theme data incorporated into InuProt.

---

## 1. Human Theme (VS Code) — Human High Contrast variant

InuProt Dark is a derivative of the **Human High Contrast** color theme
contained in Human Theme.

- Upstream repository: https://github.com/tom-f-hall/human-theme-vscode
- Upstream license: MIT
- Used in: `vscode/themes/inuprot-dark.json` (background, UI colors, TextMate
  rules, semantic token colors), and the Sublime Text derivatives
  `sublime/InuProt Dark.tmTheme` and `sublime/InuProt Dark.sublime-color-scheme`.

Modifications made in InuProt Dark: only the green ramp was changed
(`#00FF00 → #00AA00`, `#00EE00 → #009900`, `#00DD00 → #008800`) for better
separation from the orange/yellow control-flow + string colors. All other
colors and token rules are unchanged.

Original notice:

```
MIT License

Copyright (c) Tom Hall

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 2. Visual Studio Code — built-in theme-defaults (2026 Light + chain)

InuProt Light is a derivative of VS Code's built-in **2026 Light** theme,
along with its include chain `light_modern.json → light_plus.json →
light_vs.json`, which are part of the `theme-defaults` extension shipped with
VS Code.

- Upstream repository: https://github.com/microsoft/vscode
- Upstream license: MIT
- Used in: `vscode/themes/inuprot-light.json` and the bundled
  `light_modern.json`, `light_plus.json`, `light_vs.json`, and the Sublime
  Text derivatives `sublime/InuProt Light.tmTheme` and
  `sublime/InuProt Light.sublime-color-scheme`.

Modifications made in InuProt Light: only background surfaces were retinted
(`#FFFFFF → #edf3eb` for editor/gutter/active tab; `#FAFAFD → #e6eee4` for
chrome surfaces; `#F0F0F3 → #dfe7dd` for sticky-hover/no-folder). Syntax
token colors are inherited unchanged from the upstream include chain.

Original notice (from `microsoft/vscode`):

```
Copyright (c) Electron contributors
Copyright (c) 2013-2020 GitHub Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
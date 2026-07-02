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

## 2. GitHub VS Code Theme — GitHub Light Colorblind

InuProt Light is a derivative of the **GitHub Light Colorblind** theme from the
GitHub VS Code Theme extension.

- Upstream repository: https://github.com/primer/github-vscode-theme
- Upstream license: MIT
- Copyright: (c) 2020 Primer
- Used in: `vscode/themes/inuprot-light.json` and the Sublime Text derivatives
  `sublime/InuProt Light.tmTheme` and
  `sublime/InuProt Light.sublime-color-scheme`.

Modifications made in InuProt Light: only background surfaces were retinted
(`#FFFFFF → #edf3eb` for editor/chrome surfaces; `#f6f8fa → #e6eee4` for
secondary chrome; `#eaeef2`/`#f3f4f6`/`#ebecf0` → `#dfe7dd` for hover states).
Syntax token colors and all non-background UI colors are inherited unchanged
from GitHub Light Colorblind.

Original notice (from `primer/github-vscode-theme`):

```
MIT License

Copyright (c) 2020 Primer

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
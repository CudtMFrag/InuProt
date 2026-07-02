# InuProt

A two-variant colour scheme pack, published for **Visual Studio Code** and
**Sublime Text**.

| Variant        | Surface       | Origins                                                            |
|----------------|---------------|-------------------------------------------------------------------|
| **InuProt Dark**  | black + ink-green   | Forked from [Human High Contrast](https://github.com/tom-f-hall/human-theme-vscode) by Tom Hall, with the green ramp dimmed for better separation from the orange control-flow / string color. |
| **InuProt Light** | soft green tint     | Forked from VS Code's built-in **2026 Light** theme (MIT, `microsoft/vscode`), with the editor surface retinted to `#edf3eb` and chrome to `#e6eee4`; the upstream syntax palette is inherited unchanged from the `light_modern → light_plus → light_vs` include chain. |

> The name InuProt is a small play on *Inu* (犬, dog) + *Prot* (protection /
> protocol). It is unrelated to any existing project.

---

## What changed from upstream?

### InuProt Dark (from Human High Contrast)
Only the **green ramp** was retuned, to lower its luminance away from the
orange/yellow control-flow + string color. Source changes are in
[`source/changes-dark.md`](source/changes-dark.md); in short:

| Token role            | Before      | After       |
|-----------------------|-------------|-------------|
| keywords / cursor / button   | `#00FF00` | `#00AA00` |
| function names / gutter added| `#00EE00` | `#009900` |
| git untracked / hint         | `#00DD00` | `#008800` |

Everything else (UI chrome, terminal ANSI, token rules) is unchanged.

### InuProt Light (from VS Code 2026 Light)
Only **background surfaces** were retinted to a soft green. Syntax token colors
are inherited unchanged via the original include chain. Source changes are in
[`source/changes-light.md`](source/changes-light.md); in short:

| Surface                              | Before      | After       |
|--------------------------------------|-------------|-------------|
| editor / gutter / active tab         | `#FFFFFF` | `#edf3eb` |
| sideBar / activityBar / statusBar / panel / titleBar / tab inactive / widgets | `#FAFAFD` | `#e6eee4` |
| sticky hover / no-folder status      | `#F0F0F3` | `#dfe7dd` |

`input.background` and `dropdown.background` stay `#FFFFFF` so white controls
still read cleanly on the green chrome.

---

## Install

### Visual Studio Code

```bash
code --install-extension ./vscode/inuprot-1.0.0.vsix
```

Or use the Command Palette → **Preferences: Color Theme** → **InuProt Dark**
or **InuProt Light**.

### Sublime Text

Copy the two files in `sublime/` into your Packages/User directory:

- `sublime/InuProt Dark.sublime-color-scheme`
- `sublime/InuProt Light.sublime-color-scheme`
- (legacy) `sublime/InuProt Dark.tmTheme` / `sublime/InuProt Light.tmTheme`

Then in `Preferences.sublime-settings`:

```jsonc
{
  "color_scheme": "InuProt Dark.sublime-color-scheme",
  "dark_color_scheme": "InuProt Dark.sublime-color-scheme",
  "light_color_scheme": "InuProt Light.sublime-color-scheme",
}
```

---

## Project layout

```
InuProt/
├── vscode/                 # VS Code extension (packaged as vsix)
│   ├── package.json
│   ├── .vscodeignore
│   └── themes/
│       ├── inuprot-dark.json
│       └── inuprot-light.json   (+ light_modern/plus/vs from upstream, for include)
├── sublime/
│   ├── InuProt Dark.sublime-color-scheme   # modern format (preferred)
│   ├── InuProt Light.sublime-color-scheme
│   ├── InuProt Dark.tmTheme                # legacy TextMate format
│   └── InuProt Light.tmTheme
└── source/                 # build scripts
    ├── vscode_to_tmtheme.py
    └── vscode_to_sublime_colorscheme.py
```

The `source/` directory contains the converters used to flatten VS Code's
theme JSON (resolving its include chain) into self-contained Sublime color
scheme files.

---

## Attribution & Licenses

This project is MIT-licensed. Both upstreams are also MIT-licensed, which
permits modification and redistribution provided the original notices are
retained. See [`LICENSE`](LICENSE) and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)
for the full notices.

- **Human Theme** (InuProt Dark upstream)
  © Tom Hall, MIT License. https://github.com/tom-f-hall/human-theme-vscode
- **VS Code theme-defaults** (InuProt Light upstream, includes 2026 Light,
  Light Modern, Light+, Light Visual Studio)
  © Microsoft / GitHub Inc., MIT License. https://github.com/microsoft/vscode
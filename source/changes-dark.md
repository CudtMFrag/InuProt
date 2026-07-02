# Dark: changes from Human High Contrast

Source: `themeConfig.ts` in `tom-f-hall/human-theme-vscode`. In InuProt the
equivalent palette lives conceptually in `vscode/themes/inuprot-dark.json`
(we ship the generated JSON; the original build-time TypeScript palette is not
re-shipped). The mapping actually applied:

## Green ramp dimmed (improves green vs. orange separation)

| Source key (Human Theme)      | Before     | After      | Used for                              |
|-------------------------------|------------|------------|--------------------------------------|
| `keywordBold`                 | `#00FF00`  | `#00AA00`  | keywords, declarations               |
| `functionMoss`                | `#00EE00`  | `#009900`  | function names                       |
| `successLight`                | `#00EE00`  | `#009900`  | success / chart green                |
| `statusGood`                  | `#00DD00`  | `#008800`  | git untracked, status good           |
| `leafLight`                   | `#00DD00`  | `#008800`  | git untracked, leaf accents          |
| `ui.focusOutline`             | `#00FF00`  | `#00AA00`  | focus outline                        |
| `diagnostic.hint`             | `#00EE00`  | `#009900`  | editor hint foreground               |

Alpha-suffixed variants (e.g. `#00FF0040`) follow automatically.

## Unchanged
- All non-green colors (red, ochre/orange, teal, blue, gray) — including the
  orange `#FFCC00` used for string / numeric / control-flow, which the green
  was specifically dimmed to better separate from.
- UI chrome background scheme (#000000 keyboard, transparent borders).
- All TextMate token scope rules and semantic token rules other than the
  green color values above.
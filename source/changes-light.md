# Light: changes from VS Code 2026 Light

`vscode/themes/inuprot-light.json` is a copy of VS Code's built-in
`2026-light.json` with the `include` chain intact (the linked
`light_modern.json` / `light_plus.json` / `light_vs.json` are bundled verbatim).

The token-color rules were **NOT** modified. Only the following background-
surface `colors` were retinted:

## Editor surfaces: pure white → soft green

| Key                               | Before     | After      |
|-----------------------------------|------------|------------|
| `editor.background`               | `#FFFFFF`  | `#edf3eb`  |
| `editorGutter.background`         | `#FFFFFF`  | `#edf3eb`  |
| `tab.activeBackground`            | `#FFFFFF`  | `#edf3eb`  |
| `tab.hoverBackground`             | `#FFFFFF`  | `#edf3eb`  |
| `breadcrumb.background`           | `#FFFFFF`  | `#edf3eb`  |
| `commandCenter.background`        | `#FFFFFF`  | `#edf3eb`  |

## Chrome surfaces: near-white → slightly deeper green

| Key                               | Before     | After      |
|-----------------------------------|------------|------------|
| `sideBar.background`              | `#FAFAFD`  | `#e6eee4`  |
| `sideBarSectionHeader.background` | `#FAFAFD`  | `#e6eee4`  |
| `activityBar.background`          | `#FAFAFD`  | `#e6eee4`  |
| `statusBar.background`            | `#FAFAFD`  | `#e6eee4`  |
| `panel.background`                | `#FAFAFD`  | `#e6eee4`  |
| `titleBar.activeBackground`       | `#FAFAFD`  | `#e6eee4`  |
| `titleBar.inactiveBackground`     | `#FAFAFD`  | `#e6eee4`  |
| `menu.background`                | `#FAFAFD`  | `#e6eee4`  |
| `tab.inactiveBackground`          | `#FAFAFD`  | `#e6eee4`  |
| `tab.unfocusedActiveBackground`   | `#FAFAFD`  | `#e6eee4`  |
| `tab.unfocusedInactiveBackground` | `#FAFAFD`  | `#e6eee4`  |
| `editorGroupHeader.tabsBackground`| `#FAFAFD`  | `#e6eee4`  |
| `editorWidget.background`         | `#FAFAFD`  | `#e6eee4`  |
| `editorSuggestWidget.background` | `#FAFAFD`  | `#e6eee4`  |
| `editorHoverWidget.background`    | `#FAFAFD`  | `#e6eee4`  |
| `peekViewEditor.background`       | `#FAFAFD`  | `#e6eee4`  |
| `peekViewResult.background`      | `#FAFAFD`  | `#e6eee4`  |
| `peekViewTitle.background`       | `#FAFAFD`  | `#e6eee4`  |
| `notifications.background`        | `#FAFAFD`  | `#e6eee4`  |
| `notificationCenterHeader.background` | `#FAFAFD` | `#e6eee4` |
| `quickInput.background`           | `#FAFAFD`  | `#e6eee4`  |
| `quickInputTitle.background`      | `#FAFAFD`  | `#e6eee4`  |
| `breadcrumbPicker.background`     | `#FAFAFD`  | `#e6eee4`  |
| `agents.background`                | `#FAFAFD`  | `#e6eee4`  |

## Slightly deeper hover / no-folder: gray → deeper green

| Key                               | Before     | After      |
|-----------------------------------|------------|------------|
| `editorStickyScrollHover.background`| `#F0F0F3` | `#dfe7dd`  |
| `statusBar.noFolderBackground`    | `#F0F0F3`  | `#dfe7dd`  |

## Unchanged (kept white)

- `input.background`, `dropdown.background` — kept `#FFFFFF` so white input
  controls still read cleanly on the green chrome.
- All token color rules and the entire `include` chain
  (`light_modern → light_plus → light_vs`) — inherited verbatim.
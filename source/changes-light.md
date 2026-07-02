# Light: changes from GitHub Light Colorblind

`vscode/themes/inuprot-light.json` is a derivative of the **GitHub Light Colorblind**
theme from the [GitHub VS Code Theme](https://github.com/primer/github-vscode-theme)
extension (© Primer / GitHub, MIT License).

The original theme is self-contained (no `include` chain), so there are no
duplicate or conflicting scope rules. The syntax token colors are kept exactly
as upstream designed them for colorblind accessibility.

## Background surfaces retinted to soft green

| Key                               | Before (GitHub) | After (InuProt) |
|-----------------------------------|-----------------|-----------------|
| `editor.background`               | `#FFFFFF`       | `#edf3eb`       |
| `editorGutter.background`         | `#FFFFFF`       | `#edf3eb`       |
| `tab.activeBackground`            | `#FFFFFF`       | `#edf3eb`       |
| `tab.hoverBackground`             | `#FFFFFF`       | `#edf3eb`       |
| `activityBar.background`          | `#FFFFFF`       | `#edf3eb`       |
| `statusBar.background`            | `#FFFFFF`       | `#edf3eb`       |
| `statusBar.noFolderBackground`    | `#FFFFFF`       | `#edf3eb`       |
| `editorWidget.background`         | `#FFFFFF`       | `#edf3eb`       |
| `notifications.background`        | `#FFFFFF`       | `#edf3eb`       |
| `quickInput.background`           | `#FFFFFF`       | `#edf3eb`       |
| `breadcrumbPicker.background`     | `#FFFFFF`       | `#edf3eb`       |
| `debugToolBar.background`         | `#FFFFFF`       | `#edf3eb`       |
| `titleBar.activeBackground`       | `#FFFFFF`       | `#edf3eb`       |
| `sideBar.background`              | `#f6f8fa`       | `#e6eee4`       |
| `sideBarSectionHeader.background` | `#f6f8fa`       | `#e6eee4`       |
| `panel.background`                | `#f6f8fa`       | `#e6eee4`       |
| `editorGroupHeader.tabsBackground`| `#f6f8fa`       | `#e6eee4`       |
| `tab.inactiveBackground`          | `#f6f8fa`       | `#e6eee4`       |
| `titleBar.inactiveBackground`     | `#f6f8fa`       | `#e6eee4`       |
| `notificationCenterHeader.background` | `#f6f8fa`   | `#e6eee4`       |
| `textBlockQuote.background`       | `#f6f8fa`       | `#e6eee4`       |
| `checkbox.background`             | `#f6f8fa`       | `#e6eee4`       |
| `welcomePage.buttonBackground`    | `#f6f8fa`       | `#e6eee4`       |
| `list.hoverBackground`            | `#eaeef2`       | `#dfe7dd`       |
| `editor.lineHighlightBackground`  | `#eaeef2`       | `#dfe7dd`       |
| `editor.wordHighlightBackground`  | `#eaeef2`       | `#dfe7dd`       |
| `tab.unfocusedHoverBackground`    | `#eaeef2`       | `#dfe7dd`       |
| `statusBarItem.remoteBackground`  | `#eaeef2`       | `#dfe7dd`       |
| `button.secondaryHoverBackground` | `#f3f4f6`       | `#dfe7dd`       |
| `welcomePage.buttonHoverBackground`| `#f3f4f6`      | `#dfe7dd`       |
| `button.secondaryBackground`      | `#ebecf0`       | `#e6eee4`       |

## Unchanged

- All syntax `tokenColors` inherited verbatim from GitHub Light Colorblind.
- `input.background`, `dropdown.background`, `dropdown.listBackground` remain
  `#FFFFFF` so white form controls stay readable on the green chrome.
- All non-background UI colors (borders, buttons, links, etc.).
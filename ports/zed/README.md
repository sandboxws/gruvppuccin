# Gruvppuccin for Zed

> Full editor theme with syntax highlighting, terminal, and git colors. Dark and light variants in one theme family.

## Install

### Drop-in theme

1. Copy the theme file:

```sh
# macOS / Linux
mkdir -p ~/.config/zed/themes
cp themes/gruvppuccin.json ~/.config/zed/themes/

# Windows
# copy themes\gruvppuccin.json %USERPROFILE%\AppData\Roaming\Zed\themes\
```

2. Restart Zed and pick the theme:
   - `cmd-k cmd-t` (macOS) / `ctrl-k ctrl-t` (Linux), then choose **Gruvppuccin Dark** or **Gruvppuccin Light**
   - Or set it in `settings.json` — see Usage below

### Dev extension

Open **Extensions**, click **Install Dev Extension**, and select the `ports/zed/` directory.

## Usage

Follow the system appearance, mirroring the Neovim port's `:set bg=dark` / `:set bg=light`:

```json
"theme": {
  "mode": "system",
  "light": "Gruvppuccin Light",
  "dark": "Gruvppuccin Dark"
}
```

Or pin one variant with `"theme": "Gruvppuccin Dark"`.

## UI mapping

Dark values shown; the light variant uses the same palette name from the light palette.

| Zed role | Hex | Palette name |
|----------|-----|-------------|
| `editor.background` | `#181a1b` | base |
| `background`, `panel.background`, `tab_bar.background` | `#141617` | mantle |
| `title_bar.inactive_background` | `#101213` | crust |
| `editor.active_line.background` | `#242424` | surface0 |
| `element.selected` | `#2e2c2b` | surface1 |
| `border`, `pane_group.border` | `#413c39` | surface2 |
| `border.focused` | `#7daea3` | sapphire |
| `pane.focused_border`, `panel.focused_border` | `#a9b665` | green |
| `editor.line_number` | `#5a524c` | overlay0 |
| `editor.active_line_number` | `#afa4cc` | lavender |
| `editor.indent_guide` / `_active` | `#2e2c2b` / `#5a524c` | surface1 / overlay0 |
| `search.match_background` | `#8dbcb0` @ 30% | sky |
| `search.active_match_background` | `#ea6962` @ 45% | red |
| `players[0].cursor` | `#e6c9a8` | rosewater |
| `players[0].selection` | `#413c39` @ 60% | surface2 |
| `version_control.added` | `#a9b665` | green |
| `version_control.modified` | `#7daea3` | sapphire |
| `version_control.deleted` | `#ea6962` | red |
| `version_control.ignored` | `#6e655a` | overlay1 |
| `error` | `#ea6962` | red |
| `warning` | `#d8a657` | yellow |
| `info` | `#7daea3` | sapphire |
| `hint` | `#8dbcb0` | sky |
| `success` | `#89b482` | teal |

## Syntax mapping

| Zed role | Hex | Palette name |
|----------|-----|-------------|
| `comment` (italic) | `#7c7269` | overlay2 |
| `string` | `#a9b665` | green |
| `string.escape`, `string.regex`, `preproc`, `punctuation.special` | `#d4879c` | pink |
| `character`, `string.documentation`, `variant`, `text.literal` | `#89b482` | teal |
| `string.special.symbol` | `#e09b8a` | flamingo |
| `keyword` (and all `keyword.*`) | `#c28fd6` | mauve |
| `function`, `tag`, `label`, `title` | `#7daea3` | sapphire |
| `function.builtin`, `constant`, `number`, `boolean`, `attribute` | `#e78a4e` | peach |
| `type`, `enum`, `constructor`, `namespace` (italic) | `#d8a657` | yellow |
| `type.builtin`, `type.interface` (italic) | `#c28fd6` | mauve |
| `variable` | `#d4be98` | text |
| `variable.parameter` | `#e07868` | maroon |
| `property`, `variable.member`, `link_text` | `#afa4cc` | lavender |
| `operator` | `#8dbcb0` | sky |
| `punctuation`, `punctuation.bracket`, `punctuation.delimiter` | `#7c7269` | overlay2 |
| `punctuation.list_marker` | `#89b482` | teal |
| `emphasis`, `emphasis.strong`, `variable.special` | `#ea6962` | red |
| `hint` (inlay hints) | `#5a524c` | overlay0 |

## Terminal mapping

| ANSI | Normal | Bright |
|------|--------|--------|
| black | crust `#101213` | surface2 `#413c39` |
| red | red `#ea6962` | flamingo `#e09b8a` |
| green | green `#a9b665` | teal `#89b482` |
| yellow | yellow `#d8a657` | peach `#e78a4e` |
| blue | sapphire `#7daea3` | lavender `#afa4cc` |
| magenta | mauve `#c28fd6` | pink `#d4879c` |
| cyan | sky `#8dbcb0` | sky `#8dbcb0` |
| white | subtext0 `#a69a8a` | text `#d4be98` |

## Notes

- Every color is a `palette.json` hex plus a two-digit alpha suffix. The repo's `check-palette-consistency.sh` hook reads the first six digits of each literal, so translucency is expressed as alpha for Zed's compositor rather than pre-blended RGB. Transparent is written as the base color at `00`, never `#00000000`.
- `players[0].selection` is surface2 at 60%, which composites to roughly surface1 over *both* the dark and light base — reproducing the Neovim port's `Visual` highlight while staying translucent so overlapping selections and search matches still stack.
- Bright ANSI colors reuse the nearest lighter palette member, since the palette has no brightened tier. Only four cool hues exist, so `bright_cyan` repeats `cyan`. Dim variants are the normal color at 60%.
- ANSI black maps to crust `#101213`, the nearest palette member to the Neovim port's `blend(base, 0.8, black)` = `#131516`.
- `punctuation.delimiter` follows the Neovim port's explicit `Delimiter` and `@punctuation.bracket` overrides (overlay2), not the brighter `@punctuation.delimiter` default. Set it to sky `#8dbcb0` for exact Treesitter parity.
- Zed has no per-language syntax keys, so the Neovim port's Go de-emphasis block and its Rust lifetime / format-specifier overrides have no equivalent. Go parameters render maroon and struct fields lavender, per the global rules.
- JSON has no comments and the `check-json` hook is strict, so unlike the other ports this file carries no comment header — provenance lives in the `name` and `author` fields.
- Zed watches `~/.config/zed/themes/` and hot-reloads on write, so symlinking instead of copying gives live reload while iterating.

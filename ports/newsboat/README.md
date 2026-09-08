# Gruvppuccin for newsboat

> Warm earthy tones for the newsboat RSS reader, with article syntax highlighting.

newsboat has no hex support, so every color is quantized to its nearest xterm-256
index. **12 of the 13 flavors produce distinct output** — Macchiato and Mocha
quantize identically (both bases land on `color234`). Fewer still are *visually*
distinguishable: Nocturne Gruv differs from Macchiato by a single grayscale step.
All 13 ship anyway so the flavor set is uniform across ports.

## Install

1. Save the color file:

```sh
cp colors ~/.newsboat/colors
```

2. Include it from your newsboat config (`~/.newsboat/config`):

```
include ~/.newsboat/colors
```

## Flavors

`include` a flavor file from your newsboat config.

<!-- flavors:start -->
| Flavor | Mode | File |
|--------|------|------|
| Gruvppuccin Macchiato | dark | `gruvppuccin-macchiato.colors` |
| Gruvppuccin Mocha | dark | `gruvppuccin-mocha.colors` |
| Gruvppuccin Latte | light | `gruvppuccin-latte.colors` |
| Gruvppuccin Nebula | dark | `gruvppuccin-nebula.colors` |
| Gruvppuccin Void | dark | `gruvppuccin-void.colors` |
| Gruvppuccin Nova | light | `gruvppuccin-nova.colors` |
| Gruvppuccin Haze | light | `gruvppuccin-haze.colors` |
| Gruvbark Nebula | dark | `gruvbark-nebula.colors` |
| Gruvbark Void | dark | `gruvbark-void.colors` |
| Gruvbark Nova | light | `gruvbark-nova.colors` |
| Gruvbark Haze | light | `gruvbark-haze.colors` |
| Nocturne | dark | `gruvppuccin-nocturne.colors` |
| Nocturne Gruv | dark | `gruvppuccin-nocturne-gruv.colors` |
<!-- flavors:end -->

## Notes

- newsboat only supports named colors and 256-color codes (no hex). Each Gruvppuccin color is mapped to its nearest 256-color palette neighbor. The mapping table is documented in the file header.
- Article highlights colorize Feed/Link/Title/Date/Author headers, URLs, and reference links.

## 256-color mapping

| Palette name | Hex | 256 color |
|-------------|-----|-----------|
| text | `#d4be98` | color223 |
| base | `#181a1b` | color234 |
| surface1 | `#2e2c2b` | color236 |
| overlay0 | `#5a524c` | color240 |
| green | `#a9b665` | color142 |
| yellow | `#d8a657` | color179 |
| sapphire | `#7daea3` | color109 |
| red | `#ea6962` | color167 |
| peach | `#e78a4e` | color172 |
| mauve | `#c28fd6` | color176 |
| pink | `#d4879c` | color175 |
| teal | `#89b482` | color108 |

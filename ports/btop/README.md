# Gruvppuccin for btop

> Warm earthy tones with gradient graphs for CPU, temperature, and memory.

## Install

1. Copy the theme file:

```sh
# macOS / Linux
cp gruvppuccin.theme ~/.config/btop/themes/
```

2. Set the theme in btop:
   - Open btop, press `Esc` to open options, navigate to the theme selector
   - Or set `color_theme = "gruvppuccin"` in `~/.config/btop/btop.conf`

## Flavors

Copy any flavor into `~/.config/btop/themes/` and set `color_theme` to its stem.

<!-- flavors:start -->
| Flavor | Mode | File |
|--------|------|------|
| Gruvppuccin Macchiato | dark | `gruvppuccin-macchiato.theme` |
| Gruvppuccin Mocha | dark | `gruvppuccin-mocha.theme` |
| Gruvppuccin Latte | light | `gruvppuccin-latte.theme` |
| Gruvppuccin Nebula | dark | `gruvppuccin-nebula.theme` |
| Gruvppuccin Void | dark | `gruvppuccin-void.theme` |
| Gruvppuccin Nova | light | `gruvppuccin-nova.theme` |
| Gruvppuccin Haze | light | `gruvppuccin-haze.theme` |
| Gruvbark Nebula | dark | `gruvbark-nebula.theme` |
| Gruvbark Void | dark | `gruvbark-void.theme` |
| Gruvbark Nova | light | `gruvbark-nova.theme` |
| Gruvbark Haze | light | `gruvbark-haze.theme` |
| Nocturne | dark | `gruvppuccin-nocturne.theme` |
| Nocturne Gruv | dark | `gruvppuccin-nocturne-gruv.theme` |
<!-- flavors:end -->

## Gradients

All eight gradients are three-stop and defined by palette role, so each flavor
fills them from its own colors:

| Graph | Start | Mid | End |
|-------|-------|-----|-----|
| Temperature graph | `sapphire` | `peach` | `red` |
| CPU graph | `green` | `yellow` | `red` |
| free meter | `teal` | `green` | `yellow` |
| cached meter | `sapphire` | `sky` | `teal` |
| available meter | `yellow` | `peach` | `red` |
| used meter | `red` | `maroon` | `peach` |
| Download graph | `sky` | `sapphire` | `lavender` |
| Upload graph | `mauve` | `pink` | `flamingo` |

**Nocturne is the exception.** Its accent slots hold semantically inverted hues —
`peach` is a sky blue (`#38bdf8`), `green` a mint, `sapphire` a violet. Left alone,
the warm ramps would read as *cooling down* as usage climbs, so Nocturne overrides
`temp`, `available` and `used` to use `yellow` (amber) where the others use `peach`.
| Download | sky `#8dbcb0` | | |
| Upload | mauve `#c28fd6` | | |

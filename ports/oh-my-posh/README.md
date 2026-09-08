# Gruvppuccin for Oh My Posh

> Minimal single-line prompt with the full Gruvppuccin palette.

## Flavor switching

`gruvppuccin.omp.json` carries all 13 flavors via oh-my-posh's `palettes` feature:

```sh
export GRUVPPUCCIN_FLAVOR=nocturne
```

Unset or unrecognized falls back to Macchiato, so the file's default output is
byte-identical to the pre-1.0 single-flavor version. Single-flavor
`<stem>.omp.json` files are also provided if you'd rather point `--config` at one.

Note this prompt consumes only 8 of the 26 palette roles, on which Macchiato,
Mocha and Nocturne Gruv are identical — **11 of the 13 flavors render distinctly**.

## Install

1. Copy the theme file:

```sh
mkdir -p ~/.config/oh-my-posh/themes
cp gruvppuccin.omp.json ~/.config/oh-my-posh/themes/
```

2. Add to your `.zshrc` (or `.bashrc`):

```sh
eval "$(oh-my-posh init zsh --config ~/.config/oh-my-posh/themes/gruvppuccin.omp.json)"
```

## Flavors

`gruvppuccin.omp.json` carries every flavor — set `GRUVPPUCCIN_FLAVOR` to switch. Single-flavor files are also provided.

<!-- flavors:start -->
| Flavor | Mode | File |
|--------|------|------|
| Gruvppuccin Macchiato | dark | `gruvppuccin-macchiato.omp.json` |
| Gruvppuccin Mocha | dark | `gruvppuccin-mocha.omp.json` |
| Gruvppuccin Latte | light | `gruvppuccin-latte.omp.json` |
| Gruvppuccin Nebula | dark | `gruvppuccin-nebula.omp.json` |
| Gruvppuccin Void | dark | `gruvppuccin-void.omp.json` |
| Gruvppuccin Nova | light | `gruvppuccin-nova.omp.json` |
| Gruvppuccin Haze | light | `gruvppuccin-haze.omp.json` |
| Gruvbark Nebula | dark | `gruvbark-nebula.omp.json` |
| Gruvbark Void | dark | `gruvbark-void.omp.json` |
| Gruvbark Nova | light | `gruvbark-nova.omp.json` |
| Gruvbark Haze | light | `gruvbark-haze.omp.json` |
| Nocturne | dark | `gruvppuccin-nocturne.omp.json` |
| Nocturne Gruv | dark | `gruvppuccin-nocturne-gruv.omp.json` |
<!-- flavors:end -->

## Segments

| Segment | Color | Palette name |
|---------|-------|-------------|
| OS icon | `#a69a8a` | subtext0 |
| Username | `#7daea3` | sapphire |
| Path | `#d8a657` | yellow |
| Git (clean) | `#a9b665` | green |
| Git (dirty) | `#e78a4e` | peach |
| Git (ahead) | `#8dbcb0` | sky |
| Git (behind) | `#e09b8a` | flamingo |
| Prompt arrow | `#7c7269` | overlay2 |

## Notes

- The full Gruvppuccin palette is available in the theme's `palette` block as `p:colorname` references.
- Git status colors shift contextually via `foreground_templates`.

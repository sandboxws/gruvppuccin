# Gruvppuccin for Oh My Posh

> Minimal single-line prompt with the full Gruvppuccin palette.

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

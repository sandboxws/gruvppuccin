# Gruvppuccin for fzf

> Warm earthy tones for fzf's color scheme. Colors only — your layout settings are preserved.

## Install

Source the file in your `.zshrc` or `.bashrc`:

```sh
source /path/to/gruvppuccin.zsh
```

The script appends color flags to your existing `FZF_DEFAULT_OPTS`, so layout settings like `--height`, `--border`, and `--preview` are preserved.

## Flavors

Source `gruvppuccin.zsh` and set `GRUVPPUCCIN_FLAVOR`, or source a flavor file directly.

<!-- flavors:start -->
| Flavor | Mode | File |
|--------|------|------|
| Gruvppuccin Macchiato | dark | `gruvppuccin-macchiato.zsh` |
| Gruvppuccin Mocha | dark | `gruvppuccin-mocha.zsh` |
| Gruvppuccin Latte | light | `gruvppuccin-latte.zsh` |
| Gruvppuccin Nebula | dark | `gruvppuccin-nebula.zsh` |
| Gruvppuccin Void | dark | `gruvppuccin-void.zsh` |
| Gruvppuccin Nova | light | `gruvppuccin-nova.zsh` |
| Gruvppuccin Haze | light | `gruvppuccin-haze.zsh` |
| Gruvbark Nebula | dark | `gruvbark-nebula.zsh` |
| Gruvbark Void | dark | `gruvbark-void.zsh` |
| Gruvbark Nova | light | `gruvbark-nova.zsh` |
| Gruvbark Haze | light | `gruvbark-haze.zsh` |
| Nocturne | dark | `gruvppuccin-nocturne.zsh` |
| Nocturne Gruv | dark | `gruvppuccin-nocturne-gruv.zsh` |
<!-- flavors:end -->

## Color mapping

| fzf role | Hex | Palette name |
|----------|-----|-------------|
| `fg` | `#d4be98` | text |
| `bg` | `#181a1b` | base |
| `hl` | `#d8a657` | yellow |
| `fg+` | `#d4be98` | text |
| `bg+` | `#2e2c2b` | surface1 |
| `hl+` | `#e78a4e` | peach |
| `border` | `#413c39` | surface2 |
| `header` | `#7daea3` | sapphire |
| `gutter` | `#181a1b` | base |
| `spinner` | `#e78a4e` | peach |
| `info` | `#7daea3` | sapphire |
| `pointer` | `#c28fd6` | mauve |
| `marker` | `#d4879c` | pink |
| `prompt` | `#a9b665` | green |

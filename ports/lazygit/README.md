# Gruvppuccin for lazygit

> Warm Gruvbox × Catppuccin colors for lazygit's UI.

Covers all 12 theme keys lazygit supports (verified against `lazygit -c` on 0.64.1).

## Install

The simplest route is config layering — lazygit merges comma-separated config
files left to right, so a flavor can sit alongside your own config untouched:

```sh
export LG_CONFIG_FILE="$HOME/.config/lazygit/config.yml,/path/to/gruvppuccin-mocha.yml"
```

Or merge a flavor's `theme:` block into your config file by hand:

```sh
# macOS
~/Library/Application Support/lazygit/config.yml

# Linux
~/.config/lazygit/config.yml
```

Add the contents of `theme.yml` under the `gui:` key in your config:

```yaml
gui:
  theme:
    activeBorderColor:
      - '#a9b665'
      - bold
    # ... (see theme.yml for full config)
```

## Flavors

Point `LG_CONFIG_FILE` at a flavor file, or merge its `theme:` block into your config.

<!-- flavors:start -->
| Flavor | Mode | File |
|--------|------|------|
| Gruvppuccin Macchiato | dark | `gruvppuccin-macchiato.yml` |
| Gruvppuccin Mocha | dark | `gruvppuccin-mocha.yml` |
| Gruvppuccin Latte | light | `gruvppuccin-latte.yml` |
| Gruvppuccin Nebula | dark | `gruvppuccin-nebula.yml` |
| Gruvppuccin Void | dark | `gruvppuccin-void.yml` |
| Gruvppuccin Nova | light | `gruvppuccin-nova.yml` |
| Gruvppuccin Haze | light | `gruvppuccin-haze.yml` |
| Gruvbark Nebula | dark | `gruvbark-nebula.yml` |
| Gruvbark Void | dark | `gruvbark-void.yml` |
| Gruvbark Nova | light | `gruvbark-nova.yml` |
| Gruvbark Haze | light | `gruvbark-haze.yml` |
| Nocturne | dark | `gruvppuccin-nocturne.yml` |
| Nocturne Gruv | dark | `gruvppuccin-nocturne-gruv.yml` |
<!-- flavors:end -->

## Notes

- Active borders use green (`#a9b665`), matching the git-clean color in the Oh My Posh prompt.
- Cherry-pick and marked commits use mauve (`#c28fd6`) for a distinctive Catppuccin accent.

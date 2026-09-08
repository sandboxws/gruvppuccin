# Gruvppuccin for lazydocker

> Warm Gruvbox × Catppuccin colors for lazydocker's UI.

lazydocker's `ThemeConfig` defines exactly four keys — `activeBorderColor`,
`inactiveBorderColor`, `selectedLineBgColor` and `optionsTextColor`. Any other
key is parsed and silently ignored, so these files ship only those four.

## Install

Merge the theme into your lazydocker config file:

```sh
# macOS
~/Library/Application Support/lazydocker/config.yml

# Linux
~/.config/lazydocker/config.yml
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

Merge a flavor's `theme:` block into your config under `gui:`.

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

- lazydocker supports 4 theme keys (fewer than lazygit). Colors are consistent with the lazygit port.

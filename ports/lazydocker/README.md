# Gruvppuccin for lazydocker

> Warm Gruvbox x Catppuccin colors for lazydocker's UI.

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

## Notes

- lazydocker supports 4 theme keys (fewer than lazygit). Colors are consistent with the lazygit port.

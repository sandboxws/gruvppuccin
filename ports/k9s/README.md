# Gruvppuccin for k9s

> Full TUI skin with the complete Gruvppuccin palette for Kubernetes management.

## Install

1. Copy the skin file:

```sh
# macOS
mkdir -p ~/Library/Application\ Support/k9s/skins
cp gruvppuccin.yaml ~/Library/Application\ Support/k9s/skins/

# Linux
mkdir -p ~/.config/k9s/skins
cp gruvppuccin.yaml ~/.config/k9s/skins/
```

2. Set the skin in your k9s config:

```sh
# macOS
~/Library/Application Support/k9s/config.yaml

# Linux
~/.config/k9s/config.yaml
```

```yaml
k9s:
  ui:
    skin: gruvppuccin
```

## Flavors

Copy any flavor into your `skins/` directory and set `ui.skin` to its stem (no extension).

<!-- flavors:start -->
| Flavor | Mode | File |
|--------|------|------|
| Gruvppuccin Macchiato | dark | `gruvppuccin-macchiato.yaml` |
| Gruvppuccin Mocha | dark | `gruvppuccin-mocha.yaml` |
| Gruvppuccin Latte | light | `gruvppuccin-latte.yaml` |
| Gruvppuccin Nebula | dark | `gruvppuccin-nebula.yaml` |
| Gruvppuccin Void | dark | `gruvppuccin-void.yaml` |
| Gruvppuccin Nova | light | `gruvppuccin-nova.yaml` |
| Gruvppuccin Haze | light | `gruvppuccin-haze.yaml` |
| Gruvbark Nebula | dark | `gruvbark-nebula.yaml` |
| Gruvbark Void | dark | `gruvbark-void.yaml` |
| Gruvbark Nova | light | `gruvbark-nova.yaml` |
| Gruvbark Haze | light | `gruvbark-haze.yaml` |
| Nocturne | dark | `gruvppuccin-nocturne.yaml` |
| Nocturne Gruv | dark | `gruvppuccin-nocturne-gruv.yaml` |
<!-- flavors:end -->

## Notes

- The skin uses YAML anchors (`*text`, `*sapphire`, etc.) referencing the full palette at the top of the file. Change one anchor value and everything updates.
- Covers body, prompt, help, dialog, frame (borders, menus, crumbs, status, title), table, xray, YAML viewer, and logs.

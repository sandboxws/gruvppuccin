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

## Notes

- The skin uses YAML anchors (`*text`, `*sapphire`, etc.) referencing the full palette at the top of the file. Change one anchor value and everything updates.
- Covers body, prompt, help, dialog, frame (borders, menus, crumbs, status, title), table, xray, YAML viewer, and logs.

# Gruvppuccin for usql

> Syntax highlighting configuration for the universal SQL client.

## Install

Copy the config file:

```sh
# macOS
mkdir -p ~/Library/Application\ Support/usql
cp config.yaml ~/Library/Application\ Support/usql/

# Linux
mkdir -p ~/.config/usql
cp config.yaml ~/.config/usql/
```

## Notes

**This port is a shim, not a theme.** usql resolves `SYNTAX_HL_STYLE` through
Chroma's compiled-in style registry (`//go:embed`, no runtime disk loader), so a
custom Gruvppuccin palette cannot be loaded at all — it is Chroma's registry that
is closed, not a usql limitation that a config could work around. An unrecognized
style name fails **silently**, falling back to a near-monochrome default.

`SYNTAX_HL_OVERRIDE_BG true` also strips the background, so only accent colors
render. That collapses the 13 flavors onto their 5 accent sets, and Chroma has a
close built-in for three of them:

| Flavor | Chroma style |
|--------|--------------|
| Gruvppuccin Macchiato | `gruvbox` |
| Gruvppuccin Mocha | `gruvbox` |
| Gruvppuccin Latte | `gruvbox-light` |
| Gruvppuccin Nebula | `gruvbox` |
| Gruvppuccin Void | `gruvbox` |
| Gruvppuccin Nova | `gruvbox-light` |
| Gruvppuccin Haze | `gruvbox-light` |
| Gruvbark Nebula | `gruvbox` |
| Gruvbark Void | `gruvbox` |
| Gruvbark Nova | `gruvbox-light` |
| Gruvbark Haze | `gruvbox-light` |
| Nocturne | `catppuccin-mocha` |
| Nocturne Gruv | `gruvbox` |

Two loadable snippets are provided for the non-default styles:

```
\i /path/to/gruvppuccin-light.usql       # gruvbox-light
\i /path/to/gruvppuccin-nocturne.usql    # catppuccin-mocha
```

Genuine per-flavor color would need the five accent sets upstreamed to Chroma as
XML styles — tracked separately; it is not something this repo can ship.

- Only SQL syntax highlighting is affected — usql has no TUI chrome theming.

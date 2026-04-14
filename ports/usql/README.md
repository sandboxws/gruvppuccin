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

- usql does not support custom color palettes. This config uses Chroma's built-in `gruvbox` syntax highlighting style, which is the closest available match to Gruvppuccin.
- Only SQL syntax highlighting is affected — usql has no TUI chrome theming.

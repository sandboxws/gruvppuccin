# Gruvppuccin for lazygit

> Warm Gruvbox x Catppuccin colors for lazygit's UI.

## Install

Merge the theme into your lazygit config file:

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

## Notes

- Active borders use green (`#a9b665`), matching the git-clean color in the Oh My Posh prompt.
- Cherry-pick and marked commits use mauve (`#c28fd6`) for a distinctive Catppuccin accent.

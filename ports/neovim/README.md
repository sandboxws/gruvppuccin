# Gruvppuccin for Neovim

> Warm Gruvbox x Catppuccin blend built on the tokyonight.nvim engine. Dark and light modes.

## Prerequisites

- [tokyonight.nvim](https://github.com/folke/tokyonight.nvim)

## Install

### lazy.nvim

Copy `theme.lua` into your plugins directory:

```sh
cp theme.lua ~/.config/nvim/lua/plugins/theme.lua
```

### Other plugin managers

Load the spec returned by `theme.lua` with your manager's equivalent of lazy.nvim's plugin spec format.

## Usage

The theme activates automatically. Toggle between dark and light mode:

```vim
:set bg=dark
:set bg=light
```

## Notes

- Both palettes (dark and light) are defined inline — no external dependencies beyond tokyonight.
- Includes 60+ highlight overrides for Treesitter, LSP, blink.cmp, Snacks, DAP, and language-specific groups (Go, Swift).

# Gruvppuccin for Neovim

> Warm Gruvbox × Catppuccin blend. 13 flavors, dark and light.

Two variants ship here:

- **`theme.lua`** (recommended) — a lazy.nvim spec for
  [gruvppuccin.nvim](https://github.com/sandboxws/gruvppuccin.nvim), the standalone
  colorscheme with native flavor support and 60+ plugin integrations.
- **`tokyonight/theme.lua`** (legacy) — the original reskin of
  [tokyonight.nvim](https://github.com/folke/tokyonight.nvim), extended to all 13
  flavors. Kept so existing tokyonight-based setups keep working.

## Flavors

| Flavor | Mode |
|--------|------|
| `gruvppuccin-macchiato` | dark |
| `gruvppuccin-mocha` | dark |
| `gruvppuccin-latte` | light |
| `gruvppuccin-nebula` | dark |
| `gruvppuccin-void` | dark |
| `gruvppuccin-nova` | light |
| `gruvppuccin-haze` | light |
| `gruvbark-nebula` | dark |
| `gruvbark-void` | dark |
| `gruvbark-nova` | light |
| `gruvbark-haze` | light |
| `gruvppuccin-nocturne` | dark |
| `gruvppuccin-nocturne-gruv` | dark |

Pin one flavor, or let `&background` choose between a configured dark/light pair:

```lua
vim.g.gruvppuccin_flavor = "gruvppuccin-nebula"   -- pin one
-- or:
vim.g.gruvppuccin_dark_flavor  = "gruvppuccin-mocha"
vim.g.gruvppuccin_light_flavor = "gruvbark-haze"
```

Switch at runtime with `:Gruvppuccin <flavor>` (legacy variant).

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

- The legacy variant defines all 13 palettes inline — no dependencies beyond tokyonight.
- Its `opts` is a function, not a table: tokyonight's `load()` forces `&background`
  from `opts.style`, so a static style would drag every light flavor back to dark.
- `Util.blend(..., "#000000")` calls use hex literals as blend endpoints, not palette
  colors — that is expected and intentional.
- Includes 60+ highlight overrides for Treesitter, LSP, blink.cmp, Snacks, DAP, and language-specific groups (Go, Swift).

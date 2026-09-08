-- ────────────────────────────────────────────────────────────
--  GENERATED FILE — DO NOT EDIT
--  source: palette.json + templates/neovim/spec.lua
--  regen:  python3 scripts/generate.py
-- ────────────────────────────────────────────────────────────
-- ╭──────────────────────────────────────────────────────────╮
-- │       Gruvppuccin — Gruvbox × Catppuccin Blend           │
-- │  lazy.nvim spec for the standalone colorscheme           │
-- ╰──────────────────────────────────────────────────────────╯
--
-- Install: copy this file to ~/.config/nvim/lua/plugins/theme.lua
--
-- Available flavors:
--   gruvppuccin-macchiato        Gruvppuccin Macchiato (dark)
--   gruvppuccin-mocha            Gruvppuccin Mocha (dark)
--   gruvppuccin-latte            Gruvppuccin Latte (light)
--   gruvppuccin-nebula           Gruvppuccin Nebula (dark)
--   gruvppuccin-void             Gruvppuccin Void (dark)
--   gruvppuccin-nova             Gruvppuccin Nova (light)
--   gruvppuccin-haze             Gruvppuccin Haze (light)
--   gruvbark-nebula              Gruvbark Nebula (dark)
--   gruvbark-void                Gruvbark Void (dark)
--   gruvbark-nova                Gruvbark Nova (light)
--   gruvbark-haze                Gruvbark Haze (light)
--   gruvppuccin-nocturne         Nocturne (dark)
--   gruvppuccin-nocturne-gruv    Nocturne Gruv (dark)
--
-- Pin one flavor, or let &background choose between a dark/light pair.
-- Switch at runtime with :Gruvppuccin <flavor>.

return {
  {
    "sandboxws/gruvppuccin.nvim",
    lazy = false,
    priority = 1000,
    opts = {
      -- Used when `flavor` is nil and &background picks for you.
      dark_flavor = "gruvppuccin-macchiato",
      light_flavor = "gruvppuccin-latte",

      -- Uncomment to pin one flavor regardless of &background:
      -- flavor = "gruvppuccin-nebula",

      transparent = false,
      terminal_colors = true,
      styles = {
        comments = { italic = true },
        keywords = {},
        functions = {},
        variables = {},
        sidebars = "dark",
        floats = "dark",
      },
    },
    config = function(_, opts)
      require("gruvppuccin").setup(opts)
      vim.cmd.colorscheme("gruvppuccin")
    end,
  },

  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "gruvppuccin",
    },
  },
}

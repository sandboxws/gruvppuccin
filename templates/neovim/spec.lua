-- ╭──────────────────────────────────────────────────────────╮
-- │       Gruvppuccin — Gruvbox × Catppuccin Blend           │
-- │  lazy.nvim spec for the standalone colorscheme           │
-- ╰──────────────────────────────────────────────────────────╯
--
-- Install: copy this file to ~/.config/nvim/lua/plugins/theme.lua
--
-- Available flavors:
{@flavor_list}
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

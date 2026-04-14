-- ╭──────────────────────────────────────────────────────────╮
-- │        Gruvpuccin — Gruvbox × Catppuccin Blend          │
-- │  Warm earthy tones on Tokyonight's engine               │
-- │  Toggle dark/light:  :set bg=light  /  :set bg=dark     │
-- ╰──────────────────────────────────────────────────────────╯

-- Gruvpuccin palettes using Catppuccin-style semantic names,
-- mapped onto tokyonight's role-based color system.

local palettes = {
  -- ── Dark mode (deeper variant — former macchiato) ──────
  dark = {
    -- Surfaces
    crust    = "#101213",
    mantle   = "#141617",
    base     = "#181a1b",
    surface0 = "#242424",
    surface1 = "#2e2c2b",
    surface2 = "#413c39",
    -- Overlays
    overlay0 = "#5a524c",
    overlay1 = "#6e655a",
    overlay2 = "#7c7269",
    -- Text
    subtext0 = "#a69a8a",
    subtext1 = "#bfb3a2",
    text     = "#d4be98",
    -- Accents
    rosewater = "#e6c9a8",
    flamingo  = "#e09b8a",
    pink      = "#d4879c",
    mauve     = "#c28fd6",
    red       = "#ea6962",
    maroon    = "#e07868",
    peach     = "#e78a4e",
    yellow    = "#d8a657",
    green     = "#a9b665",
    teal      = "#89b482",
    sky       = "#8dbcb0",
    sapphire  = "#7daea3",
    blue      = "#7daea3",
    lavender  = "#afa4cc",
  },

  -- ── Light mode (former latte) ──────────────────────────
  light = {
    crust    = "#d5c4a1",
    mantle   = "#ebdbb2",
    base     = "#f2e5bc",
    surface0 = "#e0d5b1",
    surface1 = "#d5c4a1",
    surface2 = "#bdae93",
    overlay0 = "#a89984",
    overlay1 = "#928374",
    overlay2 = "#7c6f64",
    subtext0 = "#665c54",
    subtext1 = "#504945",
    text     = "#3c3836",
    rosewater = "#b58766",
    flamingo  = "#c14a4a",
    pink      = "#b16286",
    mauve     = "#8f3f71",
    red       = "#cc241d",
    maroon    = "#9d0006",
    peach     = "#d65d0e",
    yellow    = "#b57614",
    green     = "#79740e",
    teal      = "#427b58",
    sky       = "#458588",
    sapphire  = "#076678",
    blue      = "#076678",
    lavender  = "#7c5c8f",
  },
}

--- Map a Gruvpuccin palette onto tokyonight's color slots.
--- Called from on_colors (which runs after tokyonight computes
--- its derived colors, so we must set everything explicitly).
local function apply_palette(c, p)
  local Util = require("tokyonight.util")

  -- ── Background layers ─────────────────────────────────
  c.bg             = p.base
  c.bg_dark        = p.mantle
  c.bg_dark1       = p.crust
  c.bg_highlight   = p.surface0
  c.fg_gutter      = p.surface1
  c.terminal_black = p.surface2

  -- ── Foreground layers ─────────────────────────────────
  c.dark3   = p.overlay0 -- NonText, git.ignore
  c.dark5   = p.overlay1 -- Conceal
  c.comment = p.overlay2 -- Comments
  c.fg_dark = p.subtext0 -- secondary text
  c.fg      = p.text     -- primary text

  -- ── Custom keys (no native tokyonight slot) ───────────
  c.subtext1  = p.subtext1
  c.rosewater = p.rosewater

  -- ── Accent colors ─────────────────────────────────────
  -- Mapped by what tokyonight uses each slot for:
  c.red      = p.red               -- errors, @variable.builtin
  c.red1     = p.maroon            -- error (derived), diff delete source
  c.orange   = p.peach             -- Constant, CursorLineNr (overridden)
  c.yellow   = p.yellow            -- warnings, Type (via blue1)
  c.green    = p.green             -- String, Character (overridden to teal)
  c.green1   = p.lavender          -- @property, @variable.member
  c.green2   = p.teal              -- diff.add source, healthSuccess (overridden)
  c.blue     = p.sapphire          -- Function, @label, Directory, Title
  c.blue0    = p.surface2          -- bg_visual source (set directly below)
  c.blue1    = p.yellow            -- Type, Special (Special overridden to pink)
  c.blue2    = p.sapphire          -- info diagnostic source
  c.blue5    = p.sky               -- @operator, @punctuation.delimiter
  c.blue6    = p.pink              -- @string.regexp
  c.blue7    = p.surface1          -- diff.change source
  c.cyan     = p.mauve             -- Keyword (vim fallback), Include
  c.magenta  = p.mauve             -- Statement, @keyword.function, @string.escape (overridden)
  c.magenta2 = p.pink              -- flash.nvim labels
  c.purple   = p.mauve             -- @keyword
  c.teal     = p.sky               -- hint diagnostic, @markup.link (overridden)

  -- ── Derived colors ────────────────────────────────────
  -- Must set explicitly: on_colors runs after tokyonight
  -- computes these from the original palette.
  Util.bg = c.bg
  Util.fg = c.fg

  c.diff = {
    add    = Util.blend(p.green, 0.18, p.base),
    delete = Util.blend(p.red, 0.18, p.base),
    change = Util.blend(p.blue, 0.07, p.base),
    text   = Util.blend(p.blue, 0.30, p.base),
  }

  c.git = {
    add    = p.green,
    change = p.blue,
    delete = p.red,
    ignore = p.overlay1,
  }

  c.black            = Util.blend(p.base, 0.8, "#000000")
  c.border           = c.black
  c.border_highlight = Util.blend(p.sapphire, 0.8, p.base)

  c.bg_popup      = p.mantle
  c.bg_statusline = p.mantle
  c.bg_sidebar    = p.mantle
  c.bg_float      = p.mantle
  c.bg_visual     = p.surface1
  c.bg_search     = Util.blend(p.sky, 0.30, p.base)
  c.fg_sidebar    = p.subtext0
  c.fg_float      = p.text

  c.error   = p.red
  c.warning = p.yellow
  c.info    = p.sapphire
  c.hint    = p.sky
  c.todo    = p.sapphire

  c.rainbow = {
    p.red,
    p.peach,
    p.yellow,
    p.green,
    p.sapphire,
    p.lavender,
    p.mauve,
    p.pink,
  }

  c.terminal = {
    black          = c.black,
    black_bright   = p.surface2,
    red            = p.red,
    red_bright     = Util.brighten(p.red),
    green          = p.green,
    green_bright   = Util.brighten(p.green),
    yellow         = p.yellow,
    yellow_bright  = Util.brighten(p.yellow),
    blue           = p.sapphire,
    blue_bright    = Util.brighten(p.sapphire),
    magenta        = p.mauve,
    magenta_bright = Util.brighten(p.mauve),
    cyan           = p.sky,
    cyan_bright    = Util.brighten(p.sky),
    white          = p.subtext0,
    white_bright   = p.text,
  }
end

return {
  {
    "folke/tokyonight.nvim",
    lazy = false,
    priority = 1000,
    opts = {
      style = "moon",
      light_style = "day",
      terminal_colors = true,
      styles = {
        comments = { italic = true },
        keywords = {},
        functions = {},
        variables = {},
        sidebars = "dark",
        floats = "dark",
      },
      cache = true,
      plugins = { auto = true },

      on_colors = function(c)
        local p = palettes[vim.o.background == "light" and "light" or "dark"]
        apply_palette(c, p)
      end,

      on_highlights = function(hl, c)
        local p = palettes[vim.o.background == "light" and "light" or "dark"]

        -- ── Editor: Catppuccin-matching overrides ───────
        hl.Cursor       = { fg = p.base, bg = p.rosewater }
        hl.lCursor      = { fg = p.base, bg = p.rosewater }
        hl.CursorIM     = { fg = p.base, bg = p.rosewater }
        hl.CursorLineNr = { fg = p.lavender, bold = true }
        hl.Visual       = { bg = p.surface1, bold = true }
        hl.VisualNOS    = { bg = p.surface1, bold = true }
        hl.IncSearch    = { bg = require("tokyonight.util").blend(p.sky, 0.90, p.base), fg = p.mantle }
        hl.CurSearch    = { bg = p.red, fg = p.mantle }
        hl.Substitute   = { bg = p.surface1, fg = p.pink }

        -- ── Syntax: bridge catppuccin → tokyonight ──────
        hl.Identifier    = { fg = p.flamingo }
        hl.PreProc       = { fg = p.pink }
        hl.Special       = { fg = p.pink }
        hl.Character     = { fg = p.teal }
        hl.Delimiter     = { fg = p.overlay2 }
        hl.Todo          = { bg = p.flamingo, fg = p.base, bold = true }
        hl.healthSuccess = { fg = p.teal }

        -- ── Treesitter overrides ────────────────────────
        -- Only where tokyonight's slot mapping diverges
        -- from catppuccin's defaults.
        hl["@constructor"]           = { fg = p.yellow }
        hl["@constructor.lua"]       = { link = "@punctuation.bracket" }
        hl["@variable.parameter"]    = { fg = p.maroon }
        hl["@variable.member"]       = { fg = p.lavender }
        hl["@string.escape"]         = { fg = p.pink }
        hl["@string.regexp"]         = { fg = p.pink }
        hl["@string.documentation"]  = { fg = p.teal }
        hl["@string.special.symbol"] = { fg = p.flamingo }
        hl["@type.builtin"]          = { fg = p.mauve }
        hl["@function.builtin"]      = { fg = p.peach }
        hl["@function.macro"]        = { fg = p.pink }
        hl["@constant.builtin"]      = { fg = p.peach }
        hl["@attribute"]             = { link = "Constant" }
        hl["@module"]                = { fg = p.yellow, italic = true }
        hl["@tag"]                   = { fg = p.blue }
        hl["@tag.builtin"]           = { fg = p.blue }
        hl["@tag.attribute"]         = { fg = p.yellow, italic = true }
        hl["@tag.delimiter"]         = { fg = p.teal }
        hl["@punctuation.bracket"]   = { fg = p.overlay2 }
        hl["@punctuation.special"]   = { link = "Special" }
        hl["@markup.strong"]         = { fg = p.red, bold = true }
        hl["@markup.italic"]         = { fg = p.red, italic = true }
        hl["@markup.link"]           = { fg = p.lavender }
        hl["@markup.link.label"]     = { fg = p.lavender }
        hl["@markup.list"]           = { fg = p.teal }
        hl["@markup.list.checked"]   = { fg = p.green }
        hl["@markup.list.unchecked"] = { fg = p.overlay1 }
        hl["@markup.quote"]          = { fg = p.pink }
        hl["@comment.error"]         = { fg = p.base, bg = p.red }
        hl["@comment.warning"]       = { fg = p.base, bg = p.yellow }
        hl["@comment.hint"]          = { fg = p.base, bg = p.blue }
        hl["@comment.todo"]          = { fg = p.base, bg = p.flamingo }
        hl["@comment.note"]          = { fg = p.base, bg = p.rosewater }

        -- ── Snacks picker ──────────────────────────────
        hl.SnacksPickerDir         = { fg = p.overlay2 }
        hl.SnacksPickerFile        = { fg = p.text }
        hl.SnacksPickerPathHidden  = { fg = p.overlay1 }
        hl.SnacksPickerPathIgnored = { fg = p.overlay0 }
        hl.SnacksPickerMatch       = { fg = p.sapphire, bold = true }
        hl.SnacksPickerSelected    = { fg = p.text, bg = p.surface1 }

        -- ── Snacks UI ──────────────────────────────────
        hl.SnacksDashboardSeparator = { fg = p.surface1 }
        hl.SnacksIndent             = { fg = p.surface1 }
        hl.SnacksIndentScope        = { fg = p.overlay0 }

        -- ── Completion (blink.cmp) ─────────────────────
        hl.BlinkCmpMenu          = { fg = p.subtext1, bg = p.mantle }
        hl.BlinkCmpMenuBorder    = { fg = p.surface2, bg = p.mantle }
        hl.BlinkCmpMenuSelection = { fg = p.text, bg = p.surface1 }
        hl.BlinkCmpDoc           = { fg = p.subtext1, bg = p.mantle }
        hl.BlinkCmpDocBorder     = { fg = p.surface2, bg = p.mantle }
        hl.BlinkCmpLabel         = { fg = p.subtext1 }
        hl.BlinkCmpLabelMatch    = { fg = p.sapphire, bold = true }

        -- ── LSP refinements ────────────────────────────
        hl.LspInlayHint = { fg = p.overlay0, bg = "NONE" }
        hl.FloatTitle   = { fg = p.text, bg = p.mantle, bold = true }

        -- ── Go: de-emphasize params & struct fields ────
        hl["@lsp.type.parameter.go"]           = { link = "Identifier" }
        hl["@variable.parameter.go"]           = { link = "Identifier" }
        hl["@lsp.typemod.parameter.number.go"] = { fg = p.text }
        hl["@lsp.mod.number.go"]               = { fg = p.text }
        hl["@lsp.type.property.go"]            = { fg = p.text }
        hl["@property.go"]                     = { fg = p.text }
        hl["@field.go"]                        = { fg = p.text }  -- legacy
        hl["@variable.member.go"]              = { fg = p.text }  -- current
        hl["@variable.go"]                     = { fg = p.text }

        -- ── Swift: semantic token colors from sourcekit-lsp ──
        hl["@lsp.type.struct.swift"]        = { fg = p.yellow }
        hl["@lsp.type.class.swift"]         = { fg = p.yellow }
        hl["@lsp.type.enum.swift"]          = { fg = p.yellow }
        hl["@lsp.type.typeParameter.swift"] = { fg = p.yellow }
        hl["@lsp.type.interface.swift"]     = { fg = p.mauve, italic = true }
        hl["@lsp.type.function.swift"]      = { fg = p.blue }
        hl["@lsp.type.method.swift"]        = { fg = p.blue }
        hl["@lsp.type.property.swift"]      = { fg = p.lavender }
        hl["@lsp.type.enumMember.swift"]    = { fg = p.teal }
        hl["@lsp.type.identifier.swift"]    = { fg = p.text }

        -- ── Rust: semantic token refinements from rust-analyzer ──
        hl["@lsp.type.decorator.rust"]        = { fg = p.yellow, italic = true }
        hl["@lsp.type.deriveHelper.rust"]     = { fg = p.yellow, italic = true }
        hl["@lsp.type.lifetime.rust"]         = { fg = p.peach, italic = true }
        hl["@lsp.type.selfKeyword.rust"]      = { fg = p.red }
        hl["@lsp.type.selfTypeKeyword.rust"]  = { fg = p.yellow }
        hl["@lsp.type.formatSpecifier.rust"]  = { fg = p.pink }

        -- ── DAP Explorer ───────────────────────────────
        hl.DapExplorerScope    = { fg = p.sky, bold = true }
        hl.DapExplorerType     = { fg = p.mauve, italic = true }
        hl.DapExplorerValue    = { fg = p.green }
        hl.DapExplorerExpanded = { fg = p.peach }
      end,
    },
  },

  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "tokyonight",
    },
  },
}

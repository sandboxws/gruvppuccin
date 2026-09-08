# Changelog

## 1.0.0 — unreleased

Expands Gruvppuccin from 2 flavors to **13**, matching the JetBrains plugin, and
replaces the hand-written ports with a generator.

### Added

- **11 new flavors**, bringing this repo to parity with the IntelliJ theme:
  Gruvppuccin Mocha, Nebula, Void, Nova and Haze; Gruvbark Nebula, Void, Nova and
  Haze; Nocturne and Nocturne Gruv. The existing dark and light palettes are now
  named **Gruvppuccin Macchiato** and **Gruvppuccin Latte**.
- Every port ships all 13 flavors, named by stem (`gruvppuccin-mocha.theme`).
- `scripts/generate.py` — renders every port from `palette.json`. Python 3
  standard library only. `--check` gates CI; a pre-commit hook regenerates.
- `PALETTE.md` — generated reference for all 13 flavors × 26 roles.
- fzf gains a flavor dispatcher driven by `GRUVPPUCCIN_FLAVOR`; oh-my-posh gains
  all 13 flavors in one file via its `palettes` feature; Neovim gains a
  `:Gruvppuccin <flavor>` command.
- A second Neovim variant: `ports/neovim/theme.lua` is now a spec for the
  standalone `gruvppuccin.nvim`, with the tokyonight reskin kept at
  `ports/neovim/tokyonight/theme.lua`.

### Changed — breaking

- **Zed themes renamed.** *Gruvppuccin Dark* → **Gruvppuccin Macchiato**,
  *Gruvppuccin Light* → **Gruvppuccin Latte**, and the themes are split across
  four family files. Zed has no theme aliasing, so a `settings.json` pinning the
  old names falls back to Zed's default silently. Update it after upgrading.
- **Accent colors changed in every flavor.** The extended accents (`rosewater`,
  `flamingo`, `pink`, `maroon`, `teal`, `sky`, `lavender`) are now derived with
  the blend formula shared by `gruvppuccin-vscode`, `gruvppuccin.nvim` and
  `gruvppuccin-logseq`, rather than being hand-authored here. This repo was the
  outlier; it now matches the rest of the family. Most visible: dark `rosewater`
  moves from a pale cream `#e6c9a8` to `#e19552`.
- **Light accents realigned to the IntelliJ theme**: `red` `#cc241d` → `#d93e32`,
  `green` `#79740e` → `#8a8f1a`, `yellow` `#b57614` → `#c88c22`,
  `peach` `#d65d0e` → `#e06f1e`, `sapphire` `#076678` → `#1a7f8c`,
  `mauve` `#8f3f71` → `#a44d85`.
- **`palette.json` restructured** into `accentSets` + `flavors`. The top-level
  `dark` and `light` keys are gone; use `.flavors.macchiato.colors` and
  `.flavors.latte.colors`.
- **newsboat indices corrected.** Several were hand-picked and simply wrong —
  `text #d4be98` mapped to `color223` (`#ffd7af`) where the true nearest is
  `color180`. All indices are now computed.
- **lazygit** drops `selectedRangeBgColor` and `loadingColor`; **lazydocker**
  drops `searchingActiveBorderColor` and `defaultFgColor`. Neither program has
  ever supported those keys.
- `ports/zed/extension.toml` → `1.0.0`.

### Removed

- `scripts/check-palette-consistency.sh`, superseded by `generate.py --check`,
  which byte-compares the whole tree instead of only checking hex membership.

### Notes

- **Nocturne** does not follow the blend formula. Its accent slots hold
  semantically inverted hues (`peach` is a sky blue), so its extended accents are
  authored by hand and btop overrides three gradients to keep warm ramps warm.
- **newsboat** cannot express 13 distinct flavors: Macchiato and Mocha quantize
  to identical xterm-256 output. **usql** cannot load a custom palette at all —
  Chroma's style registry is compiled in — so it maps flavors onto the three
  closest built-in styles.

# ────────────────────────────────────────────────────────────
#  GENERATED FILE — DO NOT EDIT
#  source: palette.json + templates/fzf/flavor.tmpl
#  regen:  python3 scripts/generate.py
# ────────────────────────────────────────────────────────────
# Gruvppuccin color schemes for fzf — every flavor in one file.
#
# Source this file in your .zshrc/.bashrc:
#   source /path/to/gruvppuccin.zsh
#
# Select a flavor by exporting GRUVPPUCCIN_FLAVOR before sourcing:
#   export GRUVPPUCCIN_FLAVOR=mocha
#
# Unset or unrecognized falls back to macchiato, the pre-1.0 default, so
# sourcing this with no env var reproduces the original color set exactly.

case "${GRUVPPUCCIN_FLAVOR:-macchiato}" in
  macchiato)
    _gp_colors='--color=fg:#d4be98,bg:#181a1b,hl:#d8a657 --color=fg+:#d4be98,bg+:#2e2c2b,hl+:#e78a4e --color=border:#413c39,header:#7daea3,gutter:#181a1b --color=spinner:#e78a4e,info:#7daea3 --color=pointer:#c28fd6,marker:#d68299,prompt:#a9b665 --color=separator:#413c39,scrollbar:#5a524c --color=label:#d4be98,preview-border:#413c39'
    ;;
  mocha)
    _gp_colors='--color=fg:#d4be98,bg:#1d2021,hl:#d8a657 --color=fg+:#d4be98,bg+:#32302f,hl+:#e78a4e --color=border:#45403d,header:#7daea3,gutter:#1d2021 --color=spinner:#e78a4e,info:#7daea3 --color=pointer:#c28fd6,marker:#d68299,prompt:#a9b665 --color=separator:#45403d,scrollbar:#5a524c --color=label:#d4be98,preview-border:#45403d'
    ;;
  latte)
    _gp_colors='--color=fg:#3c3836,bg:#f2e5bc,hl:#c88c22 --color=fg+:#3c3836,bg+:#d5c4a1,hl+:#e06f1e --color=border:#bdae93,header:#1a7f8c,gutter:#f2e5bc --color=spinner:#e06f1e,info:#1a7f8c --color=pointer:#a44d85,marker:#c04e58,prompt:#8a8f1a --color=separator:#bdae93,scrollbar:#a89984 --color=label:#3c3836,preview-border:#bdae93'
    ;;
  nebula)
    _gp_colors='--color=fg:#d0d1c0,bg:#1e1e29,hl:#d8a657 --color=fg+:#d0d1c0,bg+:#312d3b,hl+:#e78a4e --color=border:#423c4b,header:#7daea3,gutter:#1e1e29 --color=spinner:#e78a4e,info:#7daea3 --color=pointer:#c28fd6,marker:#d68299,prompt:#a9b665 --color=separator:#423c4b,scrollbar:#595260 --color=label:#d0d1c0,preview-border:#423c4b'
    ;;
  void)
    _gp_colors='--color=fg:#ced8cf,bg:#1e1d2c,hl:#d8a657 --color=fg+:#ced8cf,bg+:#302c40,hl+:#e78a4e --color=border:#403a51,header:#7daea3,gutter:#1e1d2c --color=spinner:#e78a4e,info:#7daea3 --color=pointer:#c28fd6,marker:#d68299,prompt:#a9b665 --color=separator:#403a51,scrollbar:#595267 --color=label:#ced8cf,preview-border:#403a51'
    ;;
  nova)
    _gp_colors='--color=fg:#363339,bg:#f2ead2,hl:#c88c22 --color=fg+:#363339,bg+:#dbd0bd,hl+:#e06f1e --color=border:#c7beb0,header:#1a7f8c,gutter:#f2ead2 --color=spinner:#e06f1e,info:#1a7f8c --color=pointer:#a44d85,marker:#c04e58,prompt:#8a8f1a --color=separator:#c7beb0,scrollbar:#a79d98 --color=label:#363339,preview-border:#c7beb0'
    ;;
  haze)
    _gp_colors='--color=fg:#33303a,bg:#f1ecde,hl:#c88c22 --color=fg+:#33303a,bg+:#ded7cc,hl+:#e06f1e --color=border:#cdc6bf,header:#1a7f8c,gutter:#f1ecde --color=spinner:#e06f1e,info:#1a7f8c --color=pointer:#a44d85,marker:#c04e58,prompt:#8a8f1a --color=separator:#cdc6bf,scrollbar:#a69fa1 --color=label:#33303a,preview-border:#cdc6bf'
    ;;
  gruvbark-nebula)
    _gp_colors='--color=fg:#dbdfcd,bg:#282630,hl:#fabd2f --color=fg+:#dbdfcd,bg+:#403a46,hl+:#fe8019 --color=border:#524a57,header:#83a598,gutter:#282630 --color=spinner:#fe8019,info:#83a598 --color=pointer:#d3869b,marker:#e87163,prompt:#b8bb26 --color=separator:#524a57,scrollbar:#6a616c --color=label:#dbdfcd,preview-border:#524a57'
    ;;
  gruvbark-void)
    _gp_colors='--color=fg:#d5e1d7,bg:#242230,hl:#fabd2f --color=fg+:#d5e1d7,bg+:#393346,hl+:#fe8019 --color=border:#4a4358,header:#83a598,gutter:#242230 --color=spinner:#fe8019,info:#83a598 --color=pointer:#d3869b,marker:#e87163,prompt:#b8bb26 --color=separator:#4a4358,scrollbar:#635b6f --color=label:#d5e1d7,preview-border:#4a4358'
    ;;
  gruvbark-nova)
    _gp_colors='--color=fg:#363339,bg:#f7f1d9,hl:#e2aa30 --color=fg+:#363339,bg+:#e8dec8,hl+:#e06f1e --color=border:#c7beb0,header:#4f979a,gutter:#f7f1d9 --color=spinner:#e06f1e,info:#4f979a --color=pointer:#c47098,marker:#d06062,prompt:#a8a828 --color=separator:#c7beb0,scrollbar:#a79d98 --color=label:#363339,preview-border:#c7beb0'
    ;;
  gruvbark-haze)
    _gp_colors='--color=fg:#33303a,bg:#f5f1e2,hl:#e2aa30 --color=fg+:#33303a,bg+:#e7e0d2,hl+:#e06f1e --color=border:#cdc6bf,header:#4f979a,gutter:#f5f1e2 --color=spinner:#e06f1e,info:#4f979a --color=pointer:#c47098,marker:#d06062,prompt:#a8a828 --color=separator:#cdc6bf,scrollbar:#a69fa1 --color=label:#33303a,preview-border:#cdc6bf'
    ;;
  nocturne)
    _gp_colors='--color=fg:#e6e8ec,bg:#12151a,hl:#f5b454 --color=fg+:#e6e8ec,bg+:#232830,hl+:#38bdf8 --color=border:#2d333d,header:#7c6cf6,gutter:#12151a --color=spinner:#38bdf8,info:#7c6cf6 --color=pointer:#a78bfa,marker:#f472b6,prompt:#5eead4 --color=separator:#2d333d,scrollbar:#3a414d --color=label:#e6e8ec,preview-border:#2d333d'
    ;;
  nocturne-gruv)
    _gp_colors='--color=fg:#d4be98,bg:#181a1b,hl:#d8a657 --color=fg+:#d4be98,bg+:#2e2c2b,hl+:#e78a4e --color=border:#3a3836,header:#7daea3,gutter:#181a1b --color=spinner:#e78a4e,info:#7daea3 --color=pointer:#c28fd6,marker:#d68299,prompt:#a9b665 --color=separator:#3a3836,scrollbar:#4a4642 --color=label:#d4be98,preview-border:#3a3836'
    ;;
  *)
    _gp_colors='--color=fg:#d4be98,bg:#181a1b,hl:#d8a657 --color=fg+:#d4be98,bg+:#2e2c2b,hl+:#e78a4e --color=border:#413c39,header:#7daea3,gutter:#181a1b --color=spinner:#e78a4e,info:#7daea3 --color=pointer:#c28fd6,marker:#d68299,prompt:#a9b665 --color=separator:#413c39,scrollbar:#5a524c --color=label:#d4be98,preview-border:#413c39'
    ;;
esac

export FZF_DEFAULT_OPTS="${FZF_DEFAULT_OPTS:+$FZF_DEFAULT_OPTS }$_gp_colors"
unset _gp_colors

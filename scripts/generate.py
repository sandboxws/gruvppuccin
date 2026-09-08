#!/usr/bin/env python3
"""Render every Gruvppuccin port from palette.json.

palette.json is the single source of truth; everything under ports/ is generated
from it plus the templates in templates/ (the only exceptions are the port
README.md files and ports/usql/config.yaml, which carry no palette colors).

    python3 scripts/generate.py                    regenerate everything
    python3 scripts/generate.py --check            exit 1 if the tree is stale
    python3 scripts/generate.py --validate-palette check palette.json invariants
    python3 scripts/generate.py --port zed         restrict to one or more ports
    python3 scripts/generate.py --flavor nocturne  restrict to one or more flavors
"""
from __future__ import annotations

import argparse
import difflib
import json
import math
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

REPO = Path(__file__).resolve().parent.parent
PALETTE = REPO / "palette.json"
TEMPLATES = REPO / "templates"
PORTS = REPO / "ports"

STRUCTURAL = ["crust", "mantle", "base", "surface0", "surface1", "surface2",
              "overlay0", "overlay1", "overlay2", "subtext0", "subtext1", "text"]
ACCENTS = ["rosewater", "flamingo", "pink", "mauve", "red", "maroon", "peach",
           "yellow", "green", "teal", "sky", "sapphire", "blue", "lavender"]
ROLES = STRUCTURAL + ACCENTS

# `sky` anchors on the flavor's own `text`, so it varies inside an accent set and
# is deliberately absent from the accentSets block. See PALETTE.md.
SET_PINNED = [r for r in ACCENTS if r != "sky"]


# ---------------------------------------------------------------------------
# Color helpers
# ---------------------------------------------------------------------------

def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def rgb_to_hex(r: int, g: int, b: int) -> str:
    return f"#{r:02x}{g:02x}{b:02x}"


def lerp_hex(c1: str, c2: str, t: float) -> str:
    """Interpolate two hex colors.

    The floor(x + 0.5) rounding is a family invariant: gruvppuccin-vscode,
    gruvppuccin.nvim and gruvppuccin-logseq all blend this way, and their test
    suites assert byte-parity. Do not switch to round().
    """
    a, b = hex_to_rgb(c1), hex_to_rgb(c2)
    return rgb_to_hex(*(math.floor(a[i] + (b[i] - a[i]) * t + 0.5) for i in range(3)))


def _xterm256_table() -> list[tuple[int, int, int]]:
    """Indices 16-255: the 6x6x6 color cube followed by the 24-step gray ramp.

    0-15 are excluded on purpose — they are remapped by the user's terminal
    theme, so quantizing onto them would make the port look different per
    terminal.
    """
    steps = [0, 95, 135, 175, 215, 255]
    table = [(steps[r], steps[g], steps[b]) for r in range(6) for g in range(6) for b in range(6)]
    table += [(v, v, v) for v in range(8, 239, 10)]
    return table


_X256 = _xterm256_table()


def to_xterm256(h: str) -> int:
    """Nearest xterm-256 index by Euclidean RGB distance."""
    r, g, b = hex_to_rgb(h)
    best, best_d = 16, None
    for i, (cr, cg, cb) in enumerate(_X256):
        d = (r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2
        if best_d is None or d < best_d:
            best, best_d = i + 16, d
    return best


def _channel(c: int) -> float:
    s = c / 255
    return s / 12.92 if s <= 0.03928 else ((s + 0.055) / 1.055) ** 2.4


def relative_luminance(h: str) -> float:
    r, g, b = hex_to_rgb(h)
    return 0.2126 * _channel(r) + 0.7152 * _channel(g) + 0.0722 * _channel(b)


def contrast_ratio(fg: str, bg: str) -> float:
    l1, l2 = relative_luminance(fg), relative_luminance(bg)
    lo, hi = sorted((l1, l2))
    return (hi + 0.05) / (lo + 0.05)


# ---------------------------------------------------------------------------
# Palette
# ---------------------------------------------------------------------------

@dataclass
class Flavor:
    slug: str
    name: str
    stem: str
    family: str
    appearance: str
    accent_set: str
    order: int
    colors: dict[str, str]

    @property
    def is_dark(self) -> bool:
        return self.appearance == "dark"


def load_palette() -> tuple[dict, list[Flavor]]:
    data = json.loads(PALETTE.read_text())
    flavors = [
        Flavor(slug=slug, name=f["name"], stem=f["stem"], family=f["family"],
               appearance=f["appearance"], accent_set=f["accentSet"],
               order=f["order"], colors=f["colors"])
        for slug, f in data["flavors"].items()
    ]
    flavors.sort(key=lambda f: f.order)
    return data, flavors


HEX_RE = re.compile(r"^#[0-9a-f]{6}$")


def validate_palette() -> list[str]:
    data = json.loads(PALETTE.read_text())
    errors: list[str] = []
    warnings: list[str] = []
    sets = data.get("accentSets", {})
    flavors = data.get("flavors", {})

    if len(flavors) != 13:
        errors.append(f"expected 13 flavors, found {len(flavors)}")

    for sid, acc in sets.items():
        missing = [r for r in SET_PINNED if r not in acc]
        extra = [r for r in acc if r not in SET_PINNED]
        if missing:
            errors.append(f"accentSet {sid}: missing {missing}")
        if extra:
            errors.append(f"accentSet {sid}: unexpected {extra} (sky is per-flavor)")

    stems: dict[str, str] = {}
    orders: dict[int, str] = {}
    for slug, f in flavors.items():
        c = f.get("colors", {})
        missing = [r for r in ROLES if r not in c]
        extra = [r for r in c if r not in ROLES]
        if missing:
            errors.append(f"{slug}: missing roles {missing}")
        if extra:
            errors.append(f"{slug}: unknown roles {extra}")
        for r, v in c.items():
            if not HEX_RE.match(v):
                errors.append(f"{slug}.{r}: {v!r} is not lowercase #rrggbb")
        if c.get("blue") != c.get("sapphire"):
            errors.append(f"{slug}: blue {c.get('blue')} != sapphire {c.get('sapphire')}")
        if f.get("appearance") not in ("dark", "light"):
            errors.append(f"{slug}: bad appearance {f.get('appearance')!r}")
        if f.get("accentSet") not in sets:
            errors.append(f"{slug}: unknown accentSet {f.get('accentSet')!r}")
        else:
            for r, v in sets[f["accentSet"]].items():
                if c.get(r) != v:
                    errors.append(
                        f"{slug}.{r}={c.get(r)} disagrees with accentSet "
                        f"{f['accentSet']}.{r}={v}")
        if f.get("stem") in stems:
            errors.append(f"{slug}: stem {f['stem']!r} already used by {stems[f['stem']]}")
        stems[f.get("stem")] = slug
        if f.get("order") in orders:
            errors.append(f"{slug}: order {f['order']} already used by {orders[f['order']]}")
        orders[f.get("order")] = slug

        # Advisory: accents that vanish into the background.
        base = c.get("base")
        if base and HEX_RE.match(base):
            for r in ACCENTS:
                v = c.get(r)
                if v and HEX_RE.match(v) and contrast_ratio(v, base) < 2.0:
                    warnings.append(
                        f"{slug}.{r} {v} has {contrast_ratio(v, base):.2f}:1 on base {base}")

    for w in warnings:
        print(f"warning: {w}", file=sys.stderr)
    return errors


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
# The placeholder vocabulary is CLOSED: the regex only matches the 26 known role
# names and an explicit @metadata list. Every other brace in a template passes
# through untouched, which is what lets these templates carry oh-my-posh's
# "{{ .Path }}", fzf's "${FZF_DEFAULT_OPTS:+...}" and Zed's "$schema" verbatim.

META_KEYS = ["name", "slug", "stem", "family", "appearance", "order"]

_ROLE_ALT = "|".join(sorted(ROLES, key=len, reverse=True))
PLACEHOLDER = re.compile(
    r"\{(?:@(?P<meta>[a-zA-Z][a-zA-Z0-9_]*)"
    r"|(?P<role>" + _ROLE_ALT + r")"
    r"(?:\.(?P<fmt>[0-9a-fA-F]{2}|x256|rgb|hex))?)\}"
)


class TemplateError(RuntimeError):
    pass


# A leftover "{word}" after substitution is almost always a mistyped role name.
# Foreign brace syntax the templates legitimately carry is excluded: "{{ .Path }}"
# (oh-my-posh) opens with a second brace, and "${FZF_DEFAULT_OPTS:+...}" (fzf) is
# preceded by a dollar sign.
SUSPICIOUS = re.compile(r"(?<![${])\{(?P<word>[a-z][a-z0-9_]*)\}")


def render(template: str, flavor: Flavor, extras: dict[str, str] | None = None) -> str:
    extras = extras or {}

    def sub(m: re.Match) -> str:
        meta = m.group("meta")
        if meta is not None:
            if meta in extras:
                return extras[meta]
            if meta in META_KEYS:
                return str(getattr(flavor, {"slug": "slug", "name": "name", "stem": "stem",
                                            "family": "family", "appearance": "appearance",
                                            "order": "order"}[meta]))
            raise TemplateError(f"unknown metadata placeholder {{@{meta}}}")
        role, fmt = m.group("role"), m.group("fmt")
        value = flavor.colors[role]
        if fmt is None:
            return value.lstrip("#")
        if fmt == "hex":
            return value
        if fmt == "x256":
            return str(to_xterm256(value))
        if fmt == "rgb":
            return ",".join(str(c) for c in hex_to_rgb(value))
        return value.lstrip("#") + fmt.lower()  # alpha suffix

    out = PLACEHOLDER.sub(sub, template)
    leftover = SUSPICIOUS.search(out)
    if leftover:
        raise TemplateError(
            f"unresolved placeholder {{{leftover.group('word')}}} — not one of the "
            f"{len(ROLES)} known roles (did you mistype it?)")
    return out


def banner(comment: str, template_rel: str) -> str:
    rule = "─" * 60
    lines = [
        f"{comment} {rule}",
        f"{comment}  GENERATED FILE — DO NOT EDIT",
        f"{comment}  source: palette.json + {template_rel}",
        f"{comment}  regen:  python3 scripts/generate.py",
        f"{comment} {rule}",
    ]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Port registry
# ---------------------------------------------------------------------------

@dataclass
class Port:
    id: str
    template: str                      # path under templates/
    comment: str | None                # banner comment prefix; None = no banner
    out: Callable[[Flavor], Path] | None = None      # per-flavor output path
    alias: Callable[[Flavor], Path] | None = None    # legacy filename (macchiato copy)
    composite: Callable[[list[Flavor], str], dict[Path, str]] | None = None
    extras: Callable[[Flavor], dict[str, str]] | None = None

    @property
    def scope(self) -> str:
        return "composite" if self.composite else "per-flavor"


REGISTRY: list[Port] = []


def port(p: Port) -> Port:
    REGISTRY.append(p)
    return p


def build(ports: list[str] | None, flavor_filter: list[str] | None) -> dict[Path, str]:
    """Render every selected port. Returns {absolute path: content}."""
    _, flavors = load_palette()
    if flavor_filter:
        unknown = set(flavor_filter) - {f.slug for f in flavors}
        if unknown:
            raise SystemExit(f"unknown flavor(s): {', '.join(sorted(unknown))}")
        selected = [f for f in flavors if f.slug in flavor_filter]
    else:
        selected = flavors

    out: dict[Path, str] = {}
    for p in REGISTRY:
        if ports and p.id not in ports:
            continue
        tmpl = (TEMPLATES / p.template).read_text()
        if p.composite:
            out.update(p.composite(selected, tmpl))
            continue
        head = banner(p.comment, f"templates/{p.template}") if p.comment else ""
        for f in selected:
            body = render(tmpl, f, p.extras(f) if p.extras else None)
            out[p.out(f)] = head + body
            if p.alias and f.slug == "macchiato":
                note = (f"{p.comment} Alias for {f.stem} (the pre-1.0 default), kept so existing\n"
                        f"{p.comment} configs keep working. Prefer {f.stem} in new setups.\n"
                        if p.comment else "")
                out[p.alias(f)] = head + note + body
    return out


# ---------------------------------------------------------------------------
# btop
# ---------------------------------------------------------------------------
# Eight three-stop gradients. btop interpolates between the stops itself, so a
# "gradient" here is just three roles — but the role ORDER encodes a warmth
# ramp, and Nocturne breaks that: its `peach` slot holds a sky blue (#38bdf8),
# not an orange. Left alone, "memory filling up" would read as cooling down, so
# Nocturne swaps `peach` for `yellow` (amber) in the three warm ramps.

BTOP_GRADIENTS = [
    ("temp",      "Temperature graph colors",      ("sapphire", "peach", "red"),
     "cool to hot"),
    ("cpu",       "CPU graph colors",              ("green", "yellow", "red"),
     "load gradient"),
    ("free",      "Mem/Disk free meter",           ("teal", "green", "yellow"), None),
    ("cached",    "Mem/Disk cached meter",         ("sapphire", "sky", "teal"), None),
    ("available", "Mem/Disk available meter",      ("yellow", "peach", "red"), None),
    ("used",      "Mem/Disk used meter",           ("red", "maroon", "peach"), None),
    ("download",  "Download graph colors",         ("sky", "sapphire", "lavender"), None),
    ("upload",    "Upload graph colors",           ("mauve", "pink", "flamingo"), None),
]

# Nocturne only: keep the warm ramps warm.
BTOP_OVERRIDES = {
    "nocturne": {
        "temp":      ("sapphire", "yellow", "red"),
        "available": ("yellow", "maroon", "red"),
        "used":      ("red", "maroon", "yellow"),
    },
}


def btop_gradients(flavor: Flavor) -> dict[str, str]:
    overrides = BTOP_OVERRIDES.get(flavor.slug, {})
    blocks = []
    for key, label, default_stops, note in BTOP_GRADIENTS:
        stops = overrides.get(key, default_stops)
        arrow = " → ".join(stops)
        comment = f"{label} ({arrow}" + (f": {note}" if note else "") + ")"
        if key in overrides:
            comment += "\n# Nocturne override: its `peach` is a sky blue, so the warm ramp uses `yellow`"
        lines = [f"# {comment}"]
        for pos, role in zip(("start", "mid", "end"), stops):
            lines.append(f'theme[{key}_{pos}]="{flavor.colors[role]}"')
        blocks.append("\n".join(lines))
    return {"gradients": "\n\n".join(blocks)}


port(Port(
    id="btop",
    template="btop/theme.tmpl",
    comment="#",
    out=lambda f: PORTS / "btop" / f"{f.stem}.theme",
    alias=lambda f: PORTS / "btop" / "gruvppuccin.theme",
    extras=btop_gradients,
))


# ---------------------------------------------------------------------------
# lazygit / lazydocker
# ---------------------------------------------------------------------------
# Both key sets were read off the installed binaries rather than assumed:
# `lazygit -c` reports exactly 12 theme keys (selectedRangeBgColor and
# loadingColor are NOT among them), and lazydocker's ThemeConfig has exactly 4.
# The pre-expansion files carried 14 and 6 respectively; the extras were inert.

port(Port(
    id="lazygit",
    template="lazygit/theme.tmpl",
    comment="#",
    out=lambda f: PORTS / "lazygit" / f"{f.stem}.yml",
    alias=lambda f: PORTS / "lazygit" / "theme.yml",
))

port(Port(
    id="lazydocker",
    template="lazydocker/theme.tmpl",
    comment="#",
    out=lambda f: PORTS / "lazydocker" / f"{f.stem}.yml",
    alias=lambda f: PORTS / "lazydocker" / "theme.yml",
))


# ---------------------------------------------------------------------------
# newsboat
# ---------------------------------------------------------------------------

NEWSBOAT_ROLES = ["text", "base", "surface1", "overlay0", "green", "yellow",
                  "sapphire", "red", "peach", "mauve", "pink", "teal"]


def newsboat_mapping(flavor: Flavor) -> dict[str, str]:
    rows = []
    for i in range(0, len(NEWSBOAT_ROLES), 2):
        pair = NEWSBOAT_ROLES[i:i + 2]
        cells = [f"{r:<8} {flavor.colors[r]} \u2192 color{to_xterm256(flavor.colors[r]):<3}"
                 for r in pair]
        rows.append("#   " + "   ".join(cells).rstrip())
    return {"mapping": "\n".join(rows)}


port(Port(
    id="newsboat",
    template="newsboat/colors.tmpl",
    comment="#",
    out=lambda f: PORTS / "newsboat" / f"{f.stem}.colors",
    alias=lambda f: PORTS / "newsboat" / "colors",
    extras=newsboat_mapping,
))


# ---------------------------------------------------------------------------
# fzf
# ---------------------------------------------------------------------------
# Per-flavor files, plus a self-contained dispatcher that keeps the legacy
# `source .../gruvppuccin.zsh` line working. With no env var set the dispatcher
# emits exactly the macchiato options, so existing setups are unaffected.

port(Port(
    id="fzf",
    template="fzf/flavor.tmpl",
    comment="#",
    out=lambda f: PORTS / "fzf" / f"{f.stem}.zsh",
))


def _fzf_opts(flavor: Flavor, tmpl: str) -> str:
    """The single-line --color=... argument list for one flavor."""
    body = render(tmpl, flavor)
    m = re.search(r"--color=.*?\"", body, re.S)
    if not m:
        raise TemplateError("fzf template no longer contains a --color= block")
    opts = m.group(0).rstrip('"').replace("\\\n", " ")
    return " ".join(opts.split())


def fzf_dispatcher(flavors: list[Flavor], tmpl: str) -> dict[Path, str]:
    _, all_flavors = load_palette()
    default = next(f for f in all_flavors if f.slug == "macchiato")
    arms = [f"  {f.slug})\n    _gp_colors='{_fzf_opts(f, tmpl)}'\n    ;;" for f in flavors]
    arms.append(f"  *)\n    _gp_colors='{_fzf_opts(default, tmpl)}'\n    ;;")
    lines = [
        banner("#", "templates/fzf/flavor.tmpl").rstrip("\n"),
        "# Gruvppuccin color schemes for fzf — every flavor in one file.",
        "#",
        "# Source this file in your .zshrc/.bashrc:",
        "#   source /path/to/gruvppuccin.zsh",
        "#",
        "# Select a flavor by exporting GRUVPPUCCIN_FLAVOR before sourcing:",
        "#   export GRUVPPUCCIN_FLAVOR=mocha",
        "#",
        "# Unset or unrecognized falls back to macchiato, the pre-1.0 default, so",
        "# sourcing this with no env var reproduces the original color set exactly.",
        "",
        'case "${GRUVPPUCCIN_FLAVOR:-macchiato}" in',
        *arms,
        "esac",
        "",
        'export FZF_DEFAULT_OPTS="${FZF_DEFAULT_OPTS:+$FZF_DEFAULT_OPTS }$_gp_colors"',
        "unset _gp_colors",
        "",
    ]
    return {PORTS / "fzf" / "gruvppuccin.zsh": "\n".join(lines)}


port(Port(
    id="fzf-dispatcher",
    template="fzf/flavor.tmpl",
    comment=None,
    composite=fzf_dispatcher,
))


# ---------------------------------------------------------------------------
# k9s
# ---------------------------------------------------------------------------
# The skin re-declares the whole palette as YAML anchors so a user can retune one
# color and have it propagate. The block is column-aligned and role names vary
# from 3 to 9 characters, so it is emitted from code rather than substituted.
# `text` and `base` keep their k9s-facing names (foreground/background).

K9S_ANCHOR_ORDER = ["text", "base", "mantle", "crust", "surface0", "surface1", "surface2",
                    "overlay0", "overlay1", "overlay2", "subtext0", "subtext1",
                    "rosewater", "flamingo", "pink", "mauve", "red", "maroon", "peach",
                    "yellow", "green", "teal", "sky", "sapphire", "blue", "lavender"]
K9S_KEY_NAME = {"text": "foreground", "base": "background"}


def k9s_anchors(flavor: Flavor) -> dict[str, str]:
    keyw = max(len(K9S_KEY_NAME.get(r, r)) + 1 for r in K9S_ANCHOR_ORDER) + 1
    anchorw = max(len(r) for r in K9S_ANCHOR_ORDER) + 2
    lines = []
    for role in K9S_ANCHOR_ORDER:
        key = K9S_KEY_NAME.get(role, role) + ":"
        lines.append(f'{key:<{keyw}}&{role:<{anchorw - 1}}"{flavor.colors[role]}"')
    return {"anchors": "\n".join(lines)}


port(Port(
    id="k9s",
    template="k9s/skin.tmpl",
    comment="#",
    out=lambda f: PORTS / "k9s" / f"{f.stem}.yaml",
    alias=lambda f: PORTS / "k9s" / "gruvppuccin.yaml",
    extras=k9s_anchors,
))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def known_outputs(rendered: dict[Path, str]) -> set[Path]:
    return set(rendered)


def find_orphans(rendered: dict[Path, str], ports: list[str] | None) -> list[Path]:
    """Generated files still on disk that the registry no longer produces.

    Owned directories are derived from the rendered paths themselves, so a port
    whose id does not match its directory name (oh-my-posh, fzf-dispatcher) is
    still covered. Hand-maintained files are never reported.
    """
    keep = {"README.md", "config.yaml", "extension.toml"}
    # Only directories under ports/ are swept. Generated docs land at the repo
    # root alongside hand-maintained files, which are not ours to report.
    owned = {path.parent for path in rendered
             if path.parent == PORTS or PORTS in path.parent.parents}
    orphans = []
    for d in sorted(owned):
        if not d.is_dir():
            continue
        for f in sorted(d.iterdir()):
            if f.is_dir() or f.name in keep or f.suffix == ".md":
                continue
            if f not in rendered:
                orphans.append(f)
    return orphans


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="exit 1 with a diff if the tree does not match palette.json")
    ap.add_argument("--validate-palette", action="store_true",
                    help="check palette.json invariants and exit")
    ap.add_argument("--port", action="append", metavar="ID", help="restrict to a port")
    ap.add_argument("--flavor", action="append", metavar="SLUG", help="restrict to a flavor")
    ap.add_argument("--list-ports", action="store_true", help="list registered ports")
    args = ap.parse_args(argv)

    if args.list_ports:
        for p in REGISTRY:
            print(f"{p.id:<16} {p.scope:<11} templates/{p.template}")
        return 0

    errors = validate_palette()
    if errors:
        for e in errors:
            print(f"palette.json: {e}", file=sys.stderr)
        return 1
    if args.validate_palette:
        print("palette.json: OK")
        return 0

    if args.port:
        known = {p.id for p in REGISTRY}
        unknown = set(args.port) - known
        if unknown:
            print(f"unknown port(s): {', '.join(sorted(unknown))}", file=sys.stderr)
            return 2

    rendered = build(args.port, args.flavor)

    if args.check:
        stale, missing = [], []
        for path, content in sorted(rendered.items()):
            if not path.exists():
                missing.append(path)
            elif path.read_text() != content:
                stale.append(path)
        orphans = [] if args.flavor else find_orphans(rendered, args.port)
        if not (stale or missing or orphans):
            print(f"up to date ({len(rendered)} files)")
            return 0
        for path in missing:
            print(f"MISSING  {path.relative_to(REPO)}")
        for path in stale:
            rel = path.relative_to(REPO)
            print(f"STALE    {rel}")
            diff = difflib.unified_diff(
                path.read_text().splitlines(), rendered[path].splitlines(),
                f"a/{rel}", f"b/{rel}", lineterm="", n=1)
            for line in list(diff)[:12]:
                print(f"    {line}")
        for path in orphans:
            print(f"ORPHAN   {path.relative_to(REPO)}")
        print(f"\n{len(missing)} missing, {len(stale)} stale, {len(orphans)} orphaned "
              f"— run: python3 scripts/generate.py", file=sys.stderr)
        return 1

    written = 0
    for path, content in sorted(rendered.items()):
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_text() != content:
            path.write_text(content)
            written += 1
    print(f"{len(rendered)} files rendered, {written} written")
    return 0



# ---------------------------------------------------------------------------
# oh-my-posh
# ---------------------------------------------------------------------------
# oh-my-posh has a first-class multi-palette feature, so the primary artifact
# keeps its filename AND its init line and simply gains every flavor. Verified
# against oh-my-posh 31.1.2: the `palettes.template` picks by env var, and an
# unrecognized name falls back to the top-level `palette` (macchiato).
#
# The prompt itself only consumes 8 of the 26 colors, so macchiato, mocha and
# nocturne-gruv render identically — 11 visually distinct prompts, not 13. That
# is a property of this deliberately minimal prompt, not of the palette.

OMP_FLAVOR_ENV = "GRUVPPUCCIN_FLAVOR"


def _omp_doc(structure: dict, flavors: list[Flavor], default: Flavor,
             multi: bool) -> str:
    doc = {"$schema": structure["$schema"], "palette": dict(default.colors)}
    if multi:
        doc["palettes"] = {
            "template": ("{{ if .Env." + OMP_FLAVOR_ENV + " }}{{ .Env."
                         + OMP_FLAVOR_ENV + " }}{{ else }}" + default.slug + "{{ end }}"),
            "list": {f.slug: dict(f.colors) for f in flavors},
        }
    for k, v in structure.items():
        if k != "$schema":
            doc[k] = v
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


def omp_composite(flavors: list[Flavor], tmpl: str) -> dict[Path, str]:
    structure = json.loads(tmpl)
    _, all_flavors = load_palette()
    default = next(f for f in all_flavors if f.slug == "macchiato")
    out = {PORTS / "oh-my-posh" / "gruvppuccin.omp.json":
           _omp_doc(structure, flavors, default, multi=True)}
    for f in flavors:
        out[PORTS / "oh-my-posh" / f"{f.stem}.omp.json"] = _omp_doc(structure, [f], f, multi=False)
    return out


port(Port(
    id="oh-my-posh",
    template="oh-my-posh/prompt.json",
    comment=None,
    composite=omp_composite,
))


# ---------------------------------------------------------------------------
# Zed
# ---------------------------------------------------------------------------
# Zed's ThemeRegistry keys by INDIVIDUAL theme name — the family name is display
# metadata only, and duplicate theme names silently overwrite each other. So the
# 13 names must be globally unique (they are) and the families are free to be
# whatever reads best in the picker. Splitting along the family taxonomy keeps
# each file reviewable; one 13-entry array would be ~9,300 lines.
#
# The primary file keeps the name gruvppuccin.json so drop-in users who copied it
# into ~/.config/zed/themes/ overwrite in place instead of leaving a stale copy.

ZED_FAMILIES = {
    "gruvppuccin":         ("Gruvppuccin",         "gruvppuccin.json"),
    "gruvppuccin-embark":  ("Gruvppuccin Embark",  "gruvppuccin-embark.json"),
    "gruvbark":            ("Gruvbark",            "gruvbark.json"),
    "nocturne":            ("Nocturne",            "nocturne.json"),
}
ZED_SCHEMA = "https://zed.dev/schema/themes/v0.2.0.json"
ZED_AUTHOR = "Ahmed El.Hussaini"


def zed_composite(flavors: list[Flavor], tmpl: str) -> dict[Path, str]:
    grouped: dict[str, list[Flavor]] = {}
    for f in flavors:
        grouped.setdefault(f.family, []).append(f)
    out: dict[Path, str] = {}
    for family, members in grouped.items():
        display, filename = ZED_FAMILIES[family]
        doc = {
            "$schema": ZED_SCHEMA,
            "name": display,
            "author": ZED_AUTHOR,
            "themes": [json.loads(render(tmpl, f)) for f in sorted(members, key=lambda x: x.order)],
        }
        out[PORTS / "zed" / "themes" / filename] = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"
    return out


port(Port(
    id="zed",
    template="zed/theme-entry.json",
    comment=None,
    composite=zed_composite,
))


# ---------------------------------------------------------------------------
# Neovim
# ---------------------------------------------------------------------------
# Two artifacts, per the "ship both" decision:
#
#   ports/neovim/theme.lua             thin lazy.nvim spec for the standalone
#                                      colorscheme (primary; keeps the existing
#                                      `cp theme.lua ...` install working)
#   ports/neovim/tokyonight/theme.lua  the original tokyonight reskin, extended
#                                      to 13 flavors and marked legacy
#
# The tokyonight file keeps its Util.blend("#000000") anchors — those are blend
# endpoints, not palette colors, which is why .lua was validator-exempt. Under
# `--check` that exemption is no longer needed: the whole file is byte-compared.

def _lua_palettes(flavors: list[Flavor]) -> str:
    width = max(len(r) for r in ROLES)
    out = ["--- Every Gruvppuccin flavor, keyed by stem.", "local palettes = {"]
    for f in flavors:
        out.append(f"  -- \u2500\u2500 {f.name} ({f.appearance}) " + "\u2500" * max(0, 34 - len(f.name)))
        out.append(f'  ["{f.stem}"] = {{')
        for group, roles in (("Surfaces", STRUCTURAL[:6]), ("Overlays", STRUCTURAL[6:9]),
                             ("Text", STRUCTURAL[9:]), ("Accents", ACCENTS)):
            out.append(f"    -- {group}")
            for r in roles:
                out.append(f'    {r:<{width}} = "{f.colors[r]}",')
        out.append("  },")
    out.append("}")
    return "\n".join(out)


def _lua_flavors(flavors: list[Flavor]) -> str:
    width = max(len(f.stem) for f in flavors) + 2
    out = ["--- Flavor metadata: display name and which &background it wants.",
           "local flavors = {"]
    for f in flavors:
        key = f'["{f.stem}"]'
        out.append(f'  {key:<{width + 2}} = {{ name = "{f.name}", appearance = "{f.appearance}" }},')
    out.append("}")
    return "\n".join(out)


def neovim_tokyonight(flavors: list[Flavor], tmpl: str) -> dict[Path, str]:
    _, all_flavors = load_palette()
    body = tmpl.replace("{@palettes}", _lua_palettes(flavors))
    body = body.replace("{@flavors}", _lua_flavors(flavors))
    head = banner("--", "templates/neovim/tokyonight.lua")
    return {PORTS / "neovim" / "tokyonight" / "theme.lua": head + body}


def neovim_spec(flavors: list[Flavor], tmpl: str) -> dict[Path, str]:
    listing = "\n".join(
        f"--   {f.stem:<28} {f.name} ({f.appearance})" for f in flavors)
    body = tmpl.replace("{@flavor_list}", listing)
    head = banner("--", "templates/neovim/spec.lua")
    return {PORTS / "neovim" / "theme.lua": head + body}


port(Port(id="neovim", template="neovim/spec.lua", comment=None, composite=neovim_spec))
port(Port(id="neovim-tokyonight", template="neovim/tokyonight.lua", comment=None,
          composite=neovim_tokyonight))


# ---------------------------------------------------------------------------
# usql
# ---------------------------------------------------------------------------
# This port is a shim, not a theme. usql resolves SYNTAX_HL_STYLE through
# Chroma's compiled-in registry (//go:embed, no runtime disk loader), so a
# custom palette cannot be loaded — an unrecognized name silently falls back to
# Chroma's near-monochrome default. On top of that, SYNTAX_HL_OVERRIDE_BG
# strips the background, so only accents render and the 13 flavors collapse to
# their 5 accent sets. Chroma has a close built-in for three of those.
#
# ports/usql/config.yaml is deliberately NOT generated: leaving it byte-identical
# means no existing install changes.

USQL_STYLE = {
    "gruvppuccin-dark":  "gruvbox",
    "gruvbox-dark":      "gruvbox",
    "gruvppuccin-light": "gruvbox-light",
    "gruvbox-light":     "gruvbox-light",
    "nocturne":          "catppuccin-mocha",
}
# One snippet per distinct Chroma style, named for the flavor group it serves.
USQL_SNIPPETS = {
    "gruvbox-light":    ("gruvppuccin-light", "Gruvppuccin (light flavors)"),
    "catppuccin-mocha": ("gruvppuccin-nocturne", "Nocturne"),
}


def usql_composite(flavors: list[Flavor], tmpl: str) -> dict[Path, str]:
    _, all_flavors = load_palette()
    out: dict[Path, str] = {}
    for style, (stem, label) in USQL_SNIPPETS.items():
        member = next(f for f in all_flavors if USQL_STYLE[f.accent_set] == style)
        body = tmpl.replace("{@chroma}", style)
        f = Flavor(slug=stem, name=label, stem=stem, family=member.family,
                   appearance=member.appearance, accent_set=member.accent_set,
                   order=member.order, colors=member.colors)
        out[PORTS / "usql" / f"{stem}.usql"] = render(body, f)
    return out


port(Port(id="usql", template="usql/snippet.usql", comment=None, composite=usql_composite))


# ---------------------------------------------------------------------------
# Docs
# ---------------------------------------------------------------------------
# PALETTE.md is a generated reference: 13 flavors x 26 roles is 338 swatch rows,
# far too much to hand-maintain in README.md. The README keeps a compact flavor
# index and links here.

README_FILE_PATTERN = {
    "btop": "{stem}.theme", "fzf": "{stem}.zsh", "k9s": "{stem}.yaml",
    "lazygit": "{stem}.yml", "lazydocker": "{stem}.yml",
    "newsboat": "{stem}.colors", "oh-my-posh": "{stem}.omp.json",
}

ROLE_LABEL = {
    "surface0": "Surface 0", "surface1": "Surface 1", "surface2": "Surface 2",
    "overlay0": "Overlay 0", "overlay1": "Overlay 1", "overlay2": "Overlay 2",
    "subtext0": "Subtext 0", "subtext1": "Subtext 1",
}


def swatch(hex_color: str) -> str:
    fill = "%23" + hex_color.lstrip("#")
    return (f"<img src=\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' "
            f"width='16' height='16'%3E%3Crect width='16' height='16' rx='3' "
            f"fill='{fill}'/%3E%3C/svg%3E\" alt=\"{hex_color}\" />")


def docs_composite(flavors: list[Flavor], tmpl: str) -> dict[Path, str]:
    _, all_flavors = load_palette()
    data = json.loads(PALETTE.read_text())
    out = [
        "<!-- GENERATED FILE — DO NOT EDIT. Run: python3 scripts/generate.py -->",
        "", "# Gruvppuccin palette", "",
        f"{len(all_flavors)} flavors across "
        f"{len({f.family for f in all_flavors})} families, each defining the same "
        f"{len(ROLES)} roles.", "",
        "## Flavors", "",
        "| Flavor | Stem | Appearance | Family | Accent set |",
        "|--------|------|------------|--------|------------|",
    ]
    for f in all_flavors:
        out.append(f"| {f.name} | `{f.stem}` | {f.appearance} | `{f.family}` | `{f.accent_set}` |")

    out += ["", "## Accent sets", "",
            "13 of the 14 accent roles are pinned by the flavor's accent set. `sky` is the",
            "exception: it blends `sapphire` toward the flavor's own `text`, so it varies",
            "between flavors that otherwise share a set.", ""]
    for sid, acc in data["accentSets"].items():
        members = [f.name for f in all_flavors if f.accent_set == sid]
        out.append(f"**`{sid}`** — {', '.join(members)}")
        out.append("")
        out.append("| " + " | ".join(acc) + " |")
        out.append("|" + "---|" * len(acc))
        out.append("| " + " | ".join(f"`{v}`" for v in acc.values()) + " |")
        out.append("")

    out += ["## Roles by flavor", ""]
    for f in all_flavors:
        out += [f"### {f.name}", "",
                f"`{f.stem}` · {f.appearance} · accent set `{f.accent_set}`", "",
                "| Role | Color | Hex |", "|------|-------|-----|"]
        for r in ROLES:
            label = ROLE_LABEL.get(r, r.capitalize())
            out.append(f"| {label} | {swatch(f.colors[r])} | `{f.colors[r]}` |")
        out.append("")
    files = {REPO / "PALETTE.md": "\n".join(out).rstrip("\n") + "\n"}

    # The README's flavor table lives between markers so it cannot drift.
    readme_path = REPO / "README.md"
    if readme_path.exists():
        rows = ["| Flavor | Stem | Mode | Ramp | Accents |",
                "|--------|------|------|------|---------|"]
        for f in all_flavors:
            ramp = " ".join(swatch(f.colors[r]) for r in ("base", "surface1", "overlay0", "text"))
            acc = " ".join(swatch(f.colors[r])
                           for r in ("red", "peach", "yellow", "green", "sapphire", "mauve"))
            rows.append(f"| **{f.name}** | `{f.stem}` | {f.appearance} | {ramp} | {acc} |")
        block = "<!-- palette:start -->\n" + "\n".join(rows) + "\n<!-- palette:end -->"
        text = readme_path.read_text()
        pre, _, rest = text.partition("<!-- palette:start -->")
        _, _, post = rest.partition("<!-- palette:end -->")
        if pre and post:
            files[readme_path] = pre + block + post
    for port, pat in README_FILE_PATTERN.items():
        rp = PORTS / port / "README.md"
        if not rp.exists():
            continue
        rows = ["| Flavor | Mode | File |", "|--------|------|------|"]
        for f in all_flavors:
            rows.append(f"| {f.name} | {f.appearance} | `{pat.format(stem=f.stem)}` |")
        block = "<!-- flavors:start -->\n" + "\n".join(rows) + "\n<!-- flavors:end -->"
        text = rp.read_text()
        pre, _, rest = text.partition("<!-- flavors:start -->")
        _, _, post = rest.partition("<!-- flavors:end -->")
        if pre and post:
            files[rp] = pre + block + post
    return files


port(Port(id="docs", template="docs/.keep", comment=None, composite=docs_composite))


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Generate GitHub profile README SVGs — steel navy brand system (matches DESIGN.md)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "assets"
FONT = "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

# Brand tokens (portfolio DESIGN.md)
PAPER = "#F4F7FA"
INK = "#121A28"
INK_DEEP = "#080A10"
BODY = "#566374"
BORDER = "#D8E0EA"
PRIMARY = "#2A527A"
PRIMARY_HOVER = "#234568"
HIGHLIGHT = "#3878B0"
HIGHLIGHT_ON_INK = "#79B4E8"
SURFACE = "#FFFFFF"
MUTED = "#EEF2F6"


def write(rel: str, content: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print("wrote", path.relative_to(ROOT.parent))


def hero(dark: bool) -> str:
    bg = INK_DEEP if dark else SURFACE
    stroke = "#1C2636" if dark else BORDER
    name = "#F4F7FA" if dark else INK
    role = HIGHLIGHT_ON_INK if dark else PRIMARY
    sub = "#9AA6B5" if dark else BODY
    accent = HIGHLIGHT if dark else PRIMARY
    grid = "rgba(255,255,255,0.04)" if dark else "rgba(18,26,40,0.04)"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="220" viewBox="0 0 880 220" role="img" aria-labelledby="title desc">
  <title id="title">M Ubaid Javaid — Software Engineer, Full-Stack MERN / Next.js</title>
  <desc id="desc">Professional GitHub profile header for M Ubaid Javaid, Multan, Pakistan.</desc>
  <defs>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="1.2" cy="1.2" r="0.9" fill="{grid}"/>
    </pattern>
  </defs>
  <rect width="880" height="220" rx="4" fill="{bg}"/>
  <rect width="880" height="220" rx="4" fill="url(#dots)"/>
  <rect x="0.75" y="0.75" width="878.5" height="218.5" rx="3.25" fill="none" stroke="{stroke}" stroke-width="1.5"/>
  <rect x="28" y="48" width="3" height="124" fill="{accent}"/>
  <text x="48" y="58" fill="{role}" font-family="{MONO}" font-size="12" font-weight="500" letter-spacing="1.6">SOFTWARE ENGINEER · FULL-STACK</text>
  <text x="48" y="108" fill="{name}" font-family="{FONT}" font-size="42" font-weight="700" letter-spacing="-0.8">M Ubaid Javaid</text>
  <text x="48" y="142" fill="{sub}" font-family="{FONT}" font-size="16">I engineer production web products — SaaS, fintech, healthcare, and ops platforms.</text>
  <text x="48" y="168" fill="{sub}" font-family="{FONT}" font-size="14">MERN / Next.js · Multan, Pakistan · Evolvo Technologies</text>
  <g transform="translate(680 52)">
    <rect width="160" height="116" rx="2" fill="{PRIMARY if dark else MUTED}" fill-opacity="{0.35 if dark else 1}" stroke="{accent}" stroke-opacity="0.45"/>
    <text x="16" y="28" fill="{role}" font-family="{MONO}" font-size="10" letter-spacing="1.2">FOCUS</text>
    <text x="16" y="52" fill="{name}" font-family="{FONT}" font-size="13" font-weight="600">Multi-tenant SaaS</text>
    <text x="16" y="74" fill="{name}" font-family="{FONT}" font-size="13" font-weight="600">Ops dashboards</text>
    <text x="16" y="96" fill="{name}" font-family="{FONT}" font-size="13" font-weight="600">API architecture</text>
  </g>
</svg>'''


def divider(dark: bool) -> str:
    stroke = "#1C2636" if dark else BORDER
    accent = HIGHLIGHT if dark else PRIMARY
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="24" viewBox="0 0 880 24" role="presentation" aria-hidden="true">
  <line x1="0" y1="12" x2="400" y2="12" stroke="{stroke}" stroke-width="1"/>
  <rect x="432" y="9" width="16" height="6" fill="{accent}"/>
  <line x1="480" y1="12" x2="880" y2="12" stroke="{stroke}" stroke-width="1"/>
</svg>'''


def kicker(label: str, filename: str) -> None:
    write(
        f"kickers/{filename}",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="40" viewBox="0 0 880 40" role="img" aria-label="{label}">
  <rect x="0" y="18" width="28" height="3" fill="{PRIMARY}"/>
  <text x="40" y="26" fill="{PRIMARY}" font-family="{MONO}" font-size="13" font-weight="600" letter-spacing="2.2">{label.upper()}</text>
</svg>''',
    )


def button(label: str, filename: str, filled: bool = False) -> None:
    if filled:
        fill, stroke, text, icon_bg, icon_stroke = PRIMARY, PRIMARY, PAPER, PRIMARY_HOVER, PAPER
    else:
        fill, stroke, text, icon_bg, icon_stroke = SURFACE, PRIMARY, INK, PRIMARY, PAPER
    write(
        f"buttons/{filename}",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="176" height="44" viewBox="0 0 176 44" role="img" aria-label="{label}">
  <rect x="0.75" y="0.75" width="174.5" height="42.5" rx="2" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>
  <rect x="10" y="10" width="24" height="24" rx="2" fill="{icon_bg}"/>
  <path d="M18 22h8M22 18v8" stroke="{icon_stroke}" stroke-width="1.6" stroke-linecap="round"/>
  <text x="44" y="28" fill="{text}" font-family="{FONT}" font-size="14" font-weight="700">{label}</text>
</svg>''',
    )


def strip(title: str, lines: list[tuple[str, str]], filename: str, height: int = 120) -> None:
    cards = []
    n = len(lines)
    gap = 12
    pad = 20
    usable = 880 - pad * 2 - gap * (n - 1)
    w = usable / n
    y0 = 48
    for i, (h, sub) in enumerate(lines):
        x = pad + i * (w + gap)
        cards.append(
            f'''  <rect x="{x:.1f}" y="{y0}" width="{w:.1f}" height="56" rx="2" fill="{MUTED}" stroke="{BORDER}"/>
  <text x="{x + 14:.1f}" y="{y0 + 24}" fill="{INK}" font-family="{FONT}" font-size="14" font-weight="700">{h}</text>
  <text x="{x + 14:.1f}" y="{y0 + 44}" fill="{BODY}" font-family="{FONT}" font-size="12">{sub}</text>'''
        )
    write(
        filename,
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="{height}" viewBox="0 0 880 {height}" role="img" aria-labelledby="t">
  <title id="t">{title}</title>
  <rect width="880" height="{height}" rx="4" fill="{SURFACE}" stroke="{BORDER}"/>
  <text x="20" y="28" fill="{PRIMARY}" font-family="{MONO}" font-size="11" letter-spacing="1.6">{title.upper()}</text>
{chr(10).join(cards)}
</svg>''',
    )


def card(
    code: str,
    title: str,
    blurb: list[str],
    meta: str,
    filename: str,
    accent: str = PRIMARY,
) -> None:
    tspans = "\n".join(
        f'    <tspan x="24" dy="{"0" if i == 0 else "18"}">{line}</tspan>'
        for i, line in enumerate(blurb)
    )
    write(
        f"cards/{filename}",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="520" height="248" viewBox="0 0 520 248" role="img" aria-labelledby="t">
  <title id="t">{code} — {title}</title>
  <rect x="0.75" y="0.75" width="518.5" height="246.5" rx="3" fill="{SURFACE}" stroke="{BORDER}" stroke-width="1.5"/>
  <rect x="0" y="0" width="5" height="248" fill="{accent}"/>
  <text x="24" y="40" fill="{accent}" font-family="{MONO}" font-size="12" font-weight="600" letter-spacing="1.8">{code}</text>
  <text x="24" y="76" fill="{INK}" font-family="{FONT}" font-size="22" font-weight="700">{title}</text>
  <text x="24" y="102" fill="{BODY}" font-family="{FONT}" font-size="12">{meta}</text>
  <text x="24" y="138" fill="{BODY}" font-family="{FONT}" font-size="13">
{tspans}
  </text>
  <text x="24" y="222" fill="{accent}" font-family="{FONT}" font-size="13" font-weight="700">Case study →</text>
  <rect x="340" y="36" width="156" height="156" rx="2" fill="{MUTED}" stroke="{BORDER}"/>
  <rect x="364" y="68" width="108" height="12" rx="1" fill="{accent}" fill-opacity="0.85"/>
  <rect x="364" y="92" width="88" height="8" rx="1" fill="{accent}" fill-opacity="0.35"/>
  <rect x="364" y="112" width="108" height="48" rx="2" fill="{accent}" fill-opacity="0.12" stroke="{accent}" stroke-opacity="0.35"/>
  <rect x="364" y="172" width="52" height="8" rx="1" fill="{accent}" fill-opacity="0.45"/>
  <rect x="424" y="172" width="48" height="8" rx="1" fill="{accent}" fill-opacity="0.25"/>
</svg>''',
    )


def architecture() -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="320" viewBox="0 0 880 320" role="img" aria-labelledby="t d">
  <title id="t">Production system architecture</title>
  <desc id="d">Clients to edge app to API and rules to data, with tenant isolation, offline queue, and config-as-data practices from HSMS and QuikPOS-class systems.</desc>
  <rect width="880" height="320" rx="4" fill="{SURFACE}" stroke="{BORDER}"/>
  <text x="28" y="36" fill="{INK}" font-family="{FONT}" font-size="16" font-weight="700">Production system shape</text>
  <text x="28" y="56" fill="{BODY}" font-family="{FONT}" font-size="12">How HSMS / QuikPOS-class platforms are layered in practice</text>

  <rect x="28" y="84" width="170" height="86" rx="2" fill="{MUTED}" stroke="{PRIMARY}"/>
  <text x="113" y="122" text-anchor="middle" fill="{PRIMARY}" font-family="{FONT}" font-size="14" font-weight="700">Clients</text>
  <text x="113" y="144" text-anchor="middle" fill="{BODY}" font-family="{FONT}" font-size="11">Web · PWA · Admin</text>

  <text x="214" y="132" fill="{BORDER}" font-size="20">→</text>

  <rect x="238" y="84" width="170" height="86" rx="2" fill="{PAPER}" stroke="{BORDER}"/>
  <text x="323" y="122" text-anchor="middle" fill="{INK}" font-family="{FONT}" font-size="14" font-weight="700">Edge / App</text>
  <text x="323" y="144" text-anchor="middle" fill="{BODY}" font-family="{FONT}" font-size="11">Next.js · Auth · RBAC</text>

  <text x="424" y="132" fill="{BORDER}" font-size="20">→</text>

  <rect x="448" y="84" width="170" height="86" rx="2" fill="{PAPER}" stroke="{BORDER}"/>
  <text x="533" y="122" text-anchor="middle" fill="{INK}" font-family="{FONT}" font-size="14" font-weight="700">API / Rules</text>
  <text x="533" y="144" text-anchor="middle" fill="{BODY}" font-family="{FONT}" font-size="11">Express · Security rules</text>

  <text x="634" y="132" fill="{BORDER}" font-size="20">→</text>

  <rect x="658" y="84" width="190" height="86" rx="2" fill="{MUTED}" stroke="{PRIMARY}"/>
  <text x="753" y="122" text-anchor="middle" fill="{PRIMARY}" font-family="{FONT}" font-size="14" font-weight="700">Data</text>
  <text x="753" y="144" text-anchor="middle" fill="{BODY}" font-family="{FONT}" font-size="11">MongoDB · Firestore · Convex</text>

  <rect x="28" y="206" width="260" height="78" rx="2" fill="{PAPER}" stroke="{HIGHLIGHT}"/>
  <text x="48" y="240" fill="{PRIMARY}" font-family="{FONT}" font-size="14" font-weight="700">Tenant isolation</text>
  <text x="48" y="262" fill="{BODY}" font-family="{FONT}" font-size="12">Platform-enforced — not ad-hoc query filters</text>

  <rect x="308" y="206" width="260" height="78" rx="2" fill="{PAPER}" stroke="{HIGHLIGHT}"/>
  <text x="328" y="240" fill="{PRIMARY}" font-family="{FONT}" font-size="14" font-weight="700">Offline queue</text>
  <text x="328" y="262" fill="{BODY}" font-family="{FONT}" font-size="12">IndexedDB → reconcile on reconnect</text>

  <rect x="588" y="206" width="260" height="78" rx="2" fill="{PAPER}" stroke="{HIGHLIGHT}"/>
  <text x="608" y="240" fill="{PRIMARY}" font-family="{FONT}" font-size="14" font-weight="700">Config as data</text>
  <text x="608" y="262" fill="{BODY}" font-family="{FONT}" font-size="12">Workflows &amp; forms without redeploy</text>
</svg>'''


def auth_flow() -> str:
    steps = [
        ("Auth", "JWT / session"),
        ("Role", "RBAC claims"),
        ("Tenant", "Scope boundary"),
        ("Policy", "ABAC rules"),
        ("Action", "Persisted outcome"),
    ]
    parts = []
    for i, (h, s) in enumerate(steps):
        x = 28 + i * 168
        parts.append(
            f'''  <rect x="{x}" y="72" width="148" height="72" rx="2" fill="{MUTED if i in (0, 4) else PAPER}" stroke="{PRIMARY if i in (0, 4) else BORDER}"/>
  <text x="{x + 74}" y="102" text-anchor="middle" fill="{INK}" font-family="{FONT}" font-size="14" font-weight="700">{h}</text>
  <text x="{x + 74}" y="124" text-anchor="middle" fill="{BODY}" font-family="{FONT}" font-size="11">{s}</text>'''
        )
        if i < 4:
            parts.append(f'  <text x="{x + 154}" y="112" fill="{BORDER}" font-size="16">→</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="180" viewBox="0 0 880 180" role="img" aria-labelledby="t">
  <title id="t">Auth to role to tenant to policy to action</title>
  <rect width="880" height="180" rx="4" fill="{SURFACE}" stroke="{BORDER}"/>
  <text x="28" y="36" fill="{INK}" font-family="{FONT}" font-size="15" font-weight="700">Authorization path</text>
  <text x="28" y="54" fill="{BODY}" font-family="{FONT}" font-size="12">From identity to a permitted, tenant-scoped write</text>
{chr(10).join(parts)}
</svg>'''


def delivery() -> str:
    steps = ["Model", "Slice", "Harden", "Ship", "Live"]
    parts = []
    for i, s in enumerate(steps):
        x = 40 + i * 160
        parts.append(
            f'''  <circle cx="{x + 40}" cy="100" r="28" fill="{MUTED}" stroke="{PRIMARY}" stroke-width="1.5"/>
  <text x="{x + 40}" y="105" text-anchor="middle" fill="{INK}" font-family="{FONT}" font-size="13" font-weight="700">{s}</text>
  <text x="{x + 40}" y="148" text-anchor="middle" fill="{BODY}" font-family="{MONO}" font-size="11">0{i + 1}</text>'''
        )
        if i < 4:
            parts.append(
                f'  <line x1="{x + 72}" y1="100" x2="{x + 128}" y2="100" stroke="{HIGHLIGHT}" stroke-width="1.5"/>'
            )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="180" viewBox="0 0 880 180" role="img" aria-labelledby="t">
  <title id="t">Delivery loop: model, slice, harden, ship, live</title>
  <rect width="880" height="180" rx="4" fill="{SURFACE}" stroke="{BORDER}"/>
  <text x="28" y="36" fill="{INK}" font-family="{FONT}" font-size="15" font-weight="700">Delivery loop</text>
  <text x="28" y="54" fill="{BODY}" font-family="{FONT}" font-size="12">Vertical slices over half-built feature sprawl</text>
{chr(10).join(parts)}
</svg>'''


def main() -> None:
    write("hero-dark.svg", hero(True))
    write("hero-light.svg", hero(False))
    write("divider.svg", divider(False))
    write("divider-dark.svg", divider(True))

    for label, name in [
        ("Selected work", "kicker-work.svg"),
        ("Evolvo delivery", "kicker-evolvo.svg"),
        ("Stack", "kicker-stack.svg"),
        ("Experience", "kicker-system.svg"),
        ("How I work", "kicker-signal.svg"),
        ("Writing", "kicker-writing.svg"),
    ]:
        kicker(label, name)

    button("Portfolio", "btn-portfolio.svg", filled=True)
    button("Case studies", "btn-cases.svg")
    button("LinkedIn", "btn-linkedin.svg")
    button("Email", "btn-email.svg")
    button("GitHub", "btn-github.svg")

    strip(
        "Domains",
        [
            ("Fintech", "Payments · portals"),
            ("Healthcare", "Ops · clinic surfaces"),
            ("Ops / POS", "Multi-tenant retail"),
            ("Commerce", "D2C storefronts"),
        ],
        "domains-strip.svg",
    )
    strip(
        "Evidence — not invented metrics",
        [
            ("6", "Written case studies"),
            ("2", "Verified roles"),
            ("50+", "Evolvo sites attributed"),
            ("0", "Invented testimonials"),
        ],
        "proof-strip.svg",
    )
    strip(
        "Stack map",
        [
            ("Core", "TypeScript · Node.js"),
            ("Interface", "React · Next.js · Tailwind"),
            ("Server &amp; data", "Express · Mongo · Firebase"),
            ("Platform", "Vercel · Docker · GitHub"),
        ],
        "stack-strip.svg",
    )
    strip(
        "Experience",
        [
            ("Evolvo Technologies", "Feb 2026 – present"),
            ("Fiesta Content Solutions", "Jul 2024 – Jan 2026"),
        ],
        "experience-strip.svg",
        height=130,
    )
    strip(
        "Writing",
        [
            ("Next.js vs SPA", "Business websites"),
            ("Vercel vs VPS", "SaaS hosting"),
            ("Hiring Next.js", "Pakistan freelancers"),
        ],
        "writing-strip.svg",
    )
    strip(
        "Contact",
        [
            ("Email", "mubaidjavaid97@gmail.com"),
            ("Portfolio", "mubaidjavaid.vercel.app"),
            ("LinkedIn", "m-ubaid-javaid"),
        ],
        "contact-strip.svg",
    )

    card(
        "HSMS",
        "Housing Society OS",
        ["Metadata-driven workflows, plot lifecycle,", "installment billing, compliance surfaces."],
        "Multi-tenant · RBAC+ABAC · Offline PWA",
        "card-hsms.svg",
    )
    card(
        "QUIKPOS",
        "Point-of-Sale SaaS",
        ["Tenant-isolated POS with credit ledgers,", "barcode flows, and offline reconciliation."],
        "React · Vite · Firebase · Zustand",
        "card-pos.svg",
    )
    card(
        "NAAZ",
        "D2C E-Commerce",
        ["Catalog, checkout, tracking, admin, and", "receipts — SSR pages with Convex backends."],
        "Next.js · Convex · Cloudinary · PWA",
        "card-commerce.svg",
    )
    card(
        "APEX",
        "Fintech Platform",
        ["Institutional portal: payments, multicurrency,", "custody visualisation, SSR + dashboard."],
        "Next.js · TypeScript · Three.js · GSAP",
        "card-fintech.svg",
    )
    card(
        "SURGI",
        "Surgical Ops",
        ["Surgical management surfaces delivered", "as Evolvo client production work."],
        "Evolvo delivery · Live product",
        "card-surgicore.svg",
        accent=HIGHLIGHT,
    )
    card(
        "VITALIS",
        "Healthcare Platform",
        ["Clinic and admin surfaces shipped for", "healthcare operations — Evolvo delivery."],
        "Evolvo delivery · Live product",
        "card-vitalis.svg",
        accent=HIGHLIGHT,
    )

    write("diagrams/architecture.svg", architecture())
    write("diagrams/auth-flow.svg", auth_flow())
    write("diagrams/delivery.svg", delivery())
    print("done")


if __name__ == "__main__":
    main()

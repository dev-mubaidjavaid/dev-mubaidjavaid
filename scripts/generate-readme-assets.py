#!/usr/bin/env python3
"""Generate GitHub profile README SVGs with colorful original icons."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "assets"
FONT = "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

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

# Brand-accurate tech colors
C_TS = "#3178C6"
C_JS = "#F7DF1E"
C_REACT = "#61DAFB"
C_NEXT = "#111111"
C_NODE = "#339933"
C_EXPRESS = "#404040"
C_MONGO = "#47A248"
C_FIRE = "#FFCA28"
C_TAIL = "#06B6D4"
C_VERCEL = "#000000"
C_DOCKER = "#2496ED"
C_GIT = "#F05032"
C_GH = "#181717"
C_CONVEX = "#EE342F"
C_PG = "#4169E1"


def write(rel: str, content: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print("wrote", path.relative_to(ROOT.parent))


# --- Original colorful icon marks (24x24 viewBox content) ---

def icon_globe(x: float, y: float, s: float = 1, c: str = PRIMARY) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <circle cx="12" cy="12" r="10" fill="{c}"/>
  <ellipse cx="12" cy="12" rx="4" ry="10" fill="none" stroke="#fff" stroke-width="1.4"/>
  <path d="M2 12h20M4.5 7h15M4.5 17h15" fill="none" stroke="#fff" stroke-width="1.3" stroke-linecap="round"/>
</g>'''


def icon_briefcase(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <rect x="2" y="8" width="20" height="13" rx="2" fill="#D97706"/>
  <rect x="8" y="4" width="8" height="5" rx="1.5" fill="#B45309"/>
  <path d="M2 13h20" stroke="#FDE68A" stroke-width="1.5"/>
  <rect x="10" y="12" width="4" height="3" rx="0.8" fill="#FDE68A"/>
</g>'''


def icon_linkedin(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <rect width="24" height="24" rx="4" fill="#0A66C2"/>
  <path fill="#fff" d="M6.2 9.6h2.6V18H6.2V9.6zm1.3-4.2a1.5 1.5 0 110 3 1.5 1.5 0 010-3zM10.8 9.6h2.5v1.15h.04c.35-.66 1.2-1.35 2.47-1.35 2.64 0 3.13 1.74 3.13 4V18h-2.6v-3.5c0-.83-.02-1.9-1.16-1.9-1.16 0-1.34.9-1.34 1.84V18h-2.6V9.6z"/>
</g>'''


def icon_mail(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <rect x="1" y="4" width="22" height="16" rx="3" fill="#EA4335"/>
  <path d="M2 6l10 8L22 6" fill="none" stroke="#fff" stroke-width="1.8" stroke-linejoin="round"/>
  <path d="M2 18l7.5-6M22 18l-7.5-6" fill="none" stroke="#FCE8E6" stroke-width="1.2" opacity="0.7"/>
</g>'''


def icon_github(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <circle cx="12" cy="12" r="11" fill="#181717"/>
  <path fill="#fff" d="M12 4.2c-4.3 0-7.8 3.5-7.8 7.8 0 3.4 2.2 6.4 5.3 7.4.4.1.5-.2.5-.4v-1.4c-2.2.5-2.6-1-2.6-1-.4-.9-.9-1.1-.9-1.1-.7-.5.1-.5.1-.5.8.1 1.2.8 1.2.8.7 1.2 1.9.9 2.3.7.1-.5.3-.9.5-1.1-1.7-.2-3.5-.9-3.5-3.9 0-.9.3-1.6.8-2.1-.1-.2-.4-1 .1-2.1 0 0 .7-.2 2.2.8a7.5 7.5 0 014 0c1.5-1 2.2-.8 2.2-.8.5 1.1.2 1.9.1 2.1.5.6.8 1.2.8 2.1 0 3-1.8 3.7-3.5 3.9.3.3.6.7.6 1.5v2.2c0 .2.2.5.6.4A7.8 7.8 0 0019.8 12c0-4.3-3.5-7.8-7.8-7.8z"/>
</g>'''


def icon_building(x: float, y: float, s: float = 1, c: str = "#0D9488") -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <rect x="4" y="6" width="7" height="14" rx="1" fill="{c}"/>
  <rect x="13" y="3" width="7" height="17" rx="1" fill="{c}" fill-opacity="0.85"/>
  <rect x="6" y="9" width="2" height="2" fill="#ECFDF5"/>
  <rect x="9" y="9" width="2" height="2" fill="#ECFDF5"/>
  <rect x="6" y="13" width="2" height="2" fill="#ECFDF5"/>
  <rect x="9" y="13" width="2" height="2" fill="#ECFDF5"/>
  <rect x="15" y="6" width="2" height="2" fill="#CCFBF1"/>
  <rect x="18" y="6" width="2" height="2" fill="#CCFBF1"/>
  <rect x="15" y="10" width="2" height="2" fill="#CCFBF1"/>
  <rect x="18" y="10" width="2" height="2" fill="#CCFBF1"/>
  <rect x="15" y="14" width="2" height="2" fill="#CCFBF1"/>
  <rect x="7" y="17" width="3" height="3" fill="#134E4A"/>
</g>'''


def icon_pos(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <rect x="3" y="4" width="18" height="14" rx="2" fill="#7C3AED"/>
  <rect x="5" y="6" width="14" height="7" rx="1" fill="#EDE9FE"/>
  <circle cx="8" cy="16.5" r="1.2" fill="#DDD6FE"/>
  <circle cx="12" cy="16.5" r="1.2" fill="#DDD6FE"/>
  <circle cx="16" cy="16.5" r="1.2" fill="#DDD6FE"/>
  <rect x="7" y="19" width="10" height="2" rx="1" fill="#5B21B6"/>
  <path d="M7 8h8M7 10.5h5" stroke="#7C3AED" stroke-width="1.2" stroke-linecap="round"/>
</g>'''


def icon_bag(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <path d="M5 9h14l-1.2 11H6.2L5 9z" fill="#DB2777"/>
  <path d="M9 9V7a3 3 0 016 0v2" fill="none" stroke="#9D174D" stroke-width="1.8" stroke-linecap="round"/>
  <circle cx="12" cy="14" r="2" fill="#FCE7F3"/>
</g>'''


def icon_fintech(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <rect x="2" y="5" width="20" height="14" rx="3" fill="#0369A1"/>
  <rect x="2" y="8" width="20" height="3" fill="#0EA5E9"/>
  <circle cx="7" cy="15" r="1.6" fill="#E0F2FE"/>
  <rect x="11" y="13.5" width="8" height="1.4" rx="0.7" fill="#7DD3FC"/>
  <rect x="11" y="16" width="5" height="1.4" rx="0.7" fill="#38BDF8"/>
</g>'''


def icon_surgery(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <circle cx="12" cy="12" r="10" fill="#059669"/>
  <rect x="11" y="5" width="2.2" height="14" rx="1" fill="#ECFDF5"/>
  <rect x="5" y="11" width="14" height="2.2" rx="1" fill="#ECFDF5"/>
</g>'''


def icon_health(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <path d="M12 21s-7-4.4-7-10a4 4 0 017-2.6A4 4 0 0119 11c0 5.6-7 10-7 10z" fill="#E11D48"/>
  <path d="M9 11h6M12 8v6" stroke="#fff" stroke-width="1.6" stroke-linecap="round"/>
</g>'''


def icon_users(x: float, y: float, s: float = 1, c: str = PRIMARY) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <circle cx="9" cy="8" r="3.2" fill="{c}"/>
  <circle cx="16" cy="9" r="2.6" fill="{HIGHLIGHT}"/>
  <path d="M2.5 19c0-3.2 2.9-5.5 6.5-5.5S15.5 15.8 15.5 19" fill="{c}" opacity="0.9"/>
  <path d="M14 19c.3-2 1.8-3.5 4.2-3.8 2 .3 3.3 1.6 3.3 3.8" fill="{HIGHLIGHT}" opacity="0.85"/>
</g>'''


def icon_shield(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <path d="M12 2l8 3.5v6c0 5-3.4 8.4-8 10-4.6-1.6-8-5-8-10v-6L12 2z" fill="#2563EB"/>
  <path d="M8.5 12.2l2.3 2.3 4.7-5" fill="none" stroke="#DBEAFE" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
</g>'''


def icon_db(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <ellipse cx="12" cy="6" rx="8" ry="3.2" fill="#47A248"/>
  <path d="M4 6v5c0 1.8 3.6 3.2 8 3.2s8-1.4 8-3.2V6" fill="#3D8B40"/>
  <path d="M4 11v5c0 1.8 3.6 3.2 8 3.2s8-1.4 8-3.2v-5" fill="#2F6B32"/>
  <ellipse cx="12" cy="11" rx="8" ry="3.2" fill="#47A248" opacity="0.55"/>
  <ellipse cx="12" cy="16" rx="8" ry="3.2" fill="#47A248" opacity="0.35"/>
</g>'''


def icon_cloud(x: float, y: float, s: float = 1, c: str = "#0EA5E9") -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <path d="M7 17h11a4 4 0 00.4-8A6 6 0 006.2 11 3.8 3.8 0 007 17z" fill="{c}"/>
  <circle cx="9" cy="12" r="1" fill="#E0F2FE"/>
  <circle cx="13" cy="11" r="1" fill="#E0F2FE"/>
  <circle cx="17" cy="13" r="1" fill="#E0F2FE"/>
</g>'''


def icon_offline(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <rect x="4" y="3" width="16" height="18" rx="2" fill="#6366F1"/>
  <rect x="6.5" y="5.5" width="11" height="10" rx="1" fill="#EEF2FF"/>
  <circle cx="12" cy="18.5" r="1.2" fill="#C7D2FE"/>
  <path d="M9 9h6M9 12h4" stroke="#6366F1" stroke-width="1.3" stroke-linecap="round"/>
</g>'''


def icon_config(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <circle cx="12" cy="12" r="3.2" fill="#F59E0B"/>
  <path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.1 5.1l1.6 1.6M17.3 17.3l1.6 1.6M5.1 18.9l1.6-1.6M17.3 6.7l1.6-1.6" stroke="#D97706" stroke-width="2" stroke-linecap="round"/>
  <circle cx="12" cy="12" r="1.4" fill="#FEF3C7"/>
</g>'''


def icon_key(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <circle cx="9" cy="10" r="5" fill="#F59E0B"/>
  <circle cx="9" cy="10" r="2" fill="#FEF3C7"/>
  <rect x="12.5" y="8.5" width="9" height="3" rx="1.2" fill="#D97706"/>
  <rect x="18" y="11.5" width="1.8" height="3" rx="0.6" fill="#D97706"/>
  <rect x="15.2" y="11.5" width="1.8" height="2.2" rx="0.6" fill="#B45309"/>
</g>'''


def icon_role(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <rect x="4" y="4" width="16" height="16" rx="3" fill="#8B5CF6"/>
  <path d="M8 12h8M12 8v8" stroke="#EDE9FE" stroke-width="2" stroke-linecap="round"/>
</g>'''


def icon_tenant(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <rect x="3" y="5" width="8" height="14" rx="1.5" fill="#0D9488"/>
  <rect x="13" y="5" width="8" height="14" rx="1.5" fill="#14B8A6"/>
  <rect x="5" y="8" width="4" height="2" fill="#CCFBF1"/>
  <rect x="15" y="8" width="4" height="2" fill="#CCFBF1"/>
  <rect x="5" y="12" width="4" height="2" fill="#99F6E4"/>
  <rect x="15" y="12" width="4" height="2" fill="#99F6E4"/>
</g>'''


def icon_policy(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <path d="M6 3h9l5 5v13a1 1 0 01-1 1H6a1 1 0 01-1-1V4a1 1 0 011-1z" fill="#2563EB"/>
  <path d="M15 3v5h5" fill="#1D4ED8"/>
  <path d="M8 13h8M8 16h6" stroke="#DBEAFE" stroke-width="1.5" stroke-linecap="round"/>
</g>'''


def icon_action(x: float, y: float, s: float = 1) -> str:
    return f'''<g transform="translate({x} {y}) scale({s})">
  <circle cx="12" cy="12" r="10" fill="#16A34A"/>
  <path d="M7.5 12.5l3 3 6-6.5" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
</g>'''


def icon_chip(label: str, color: str, x: float, y: float, w: float = 72) -> str:
    return f'''<g transform="translate({x} {y})">
  <rect width="{w}" height="28" rx="6" fill="{color}"/>
  <text x="{w/2}" y="18" text-anchor="middle" fill="#fff" font-family="{FONT}" font-size="11" font-weight="700">{label}</text>
</g>'''


def tech_badge(name: str, color: str, mark: str, x: float, y: float) -> str:
    return f'''<g transform="translate({x} {y})">
  <rect width="64" height="56" rx="8" fill="{MUTED}" stroke="{BORDER}"/>
  <g transform="translate(20 8)">{mark}</g>
  <text x="32" y="48" text-anchor="middle" fill="{INK}" font-family="{FONT}" font-size="9" font-weight="600">{name}</text>
</g>'''


def tech_mark_react() -> str:
    return f'''<g>
  <circle cx="12" cy="12" r="2.2" fill="{C_REACT}"/>
  <ellipse cx="12" cy="12" rx="10" ry="4" fill="none" stroke="{C_REACT}" stroke-width="1.4"/>
  <ellipse cx="12" cy="12" rx="10" ry="4" fill="none" stroke="{C_REACT}" stroke-width="1.4" transform="rotate(60 12 12)"/>
  <ellipse cx="12" cy="12" rx="10" ry="4" fill="none" stroke="{C_REACT}" stroke-width="1.4" transform="rotate(120 12 12)"/>
</g>'''


def tech_mark_ts() -> str:
    return f'''<g>
  <rect width="24" height="24" rx="3" fill="{C_TS}"/>
  <text x="12" y="16" text-anchor="middle" fill="#fff" font-family="{FONT}" font-size="10" font-weight="800">TS</text>
</g>'''


def tech_mark_node() -> str:
    return f'''<g>
  <path d="M12 1.5l9 5.2v10.6L12 22.5 3 17.3V6.7L12 1.5z" fill="{C_NODE}"/>
  <text x="12" y="15" text-anchor="middle" fill="#fff" font-family="{FONT}" font-size="8" font-weight="800">N</text>
</g>'''


def tech_mark_mongo() -> str:
    return f'''<g>
  <path d="M12 2c2 4 5 6.5 5 11 0 3-2 6-5 9-3-3-5-6-5-9 0-4.5 3-7 5-11z" fill="{C_MONGO}"/>
  <path d="M12 8v12" stroke="#fff" stroke-width="1.2" stroke-linecap="round" opacity="0.5"/>
</g>'''


def tech_mark_next() -> str:
    return f'''<g>
  <circle cx="12" cy="12" r="11" fill="#111"/>
  <path d="M8 7h2.2l5.2 8.2V7H17v10h-2.1L9.6 8.7V17H8V7z" fill="#fff"/>
</g>'''


def tech_mark_tailwind() -> str:
    return f'''<g>
  <path d="M6.5 13c1.2-4 3-6 5.5-6 1.9 0 3 1 4 2.5C17 11 18 12 19.5 12c1.6 0 2.8-1 3.5-2.5C21.8 13.5 20 15.5 17.5 15.5c-1.9 0-3-1-4-2.5C12.5 11.5 11.5 10.5 10 10.5c-1.6 0-2.8 1-3.5 2.5z" fill="{C_TAIL}"/>
  <path d="M1 15.5c1.2-4 3-6 5.5-6 1.9 0 3 1 4 2.5 1 1.5 2 2.5 3.5 2.5 1.6 0 2.8-1 3.5-2.5C16.3 16 14.5 18 12 18c-1.9 0-3-1-4-2.5C7 14 6 13 4.5 13c-1.6 0-2.8 1-3.5 2.5z" fill="{C_TAIL}" opacity="0.75"/>
</g>'''


def tech_mark_firebase() -> str:
    return f'''<g>
  <path d="M6 18l2.2-12 3.2 6.2L14 5l4 13H6z" fill="{C_FIRE}"/>
  <path d="M8.2 6L6 18h4.2L8.2 6z" fill="#FFA000"/>
  <path d="M11.4 12.2L14 5l4 13h-5.2l-1.4-5.8z" fill="#F57C00"/>
</g>'''


def tech_mark_docker() -> str:
    return f'''<g>
  <rect x="3" y="11" width="4" height="3.2" rx="0.4" fill="{C_DOCKER}"/>
  <rect x="7.5" y="11" width="4" height="3.2" rx="0.4" fill="{C_DOCKER}"/>
  <rect x="12" y="11" width="4" height="3.2" rx="0.4" fill="{C_DOCKER}"/>
  <rect x="7.5" y="7" width="4" height="3.2" rx="0.4" fill="{C_DOCKER}"/>
  <rect x="12" y="7" width="4" height="3.2" rx="0.4" fill="{C_DOCKER}"/>
  <rect x="16.5" y="11" width="4" height="3.2" rx="0.4" fill="{C_DOCKER}"/>
  <path d="M3 15.5c0 2 3.5 3 9 3s9-1 9-3" fill="none" stroke="#149EED" stroke-width="1.2"/>
</g>'''


def tech_mark_vercel() -> str:
    return f'''<g>
  <path d="M12 4l9 16H3L12 4z" fill="#111"/>
</g>'''


def tech_mark_git() -> str:
    return f'''<g>
  <circle cx="6" cy="18" r="2.4" fill="{C_GIT}"/>
  <circle cx="18" cy="18" r="2.4" fill="{C_GIT}"/>
  <circle cx="12" cy="6" r="2.4" fill="{C_GIT}"/>
  <path d="M6 18l6-12 6 12" fill="none" stroke="{C_GIT}" stroke-width="2"/>
</g>'''


def tech_mark_express() -> str:
    return f'''<g>
  <rect width="24" height="24" rx="4" fill="#2D2D2D"/>
  <text x="12" y="15.5" text-anchor="middle" fill="#fff" font-family="{FONT}" font-size="7" font-weight="700">ex</text>
</g>'''


def hero(dark: bool) -> str:
    bg = INK_DEEP if dark else SURFACE
    stroke = "#1C2636" if dark else BORDER
    name = "#F4F7FA" if dark else INK
    role = HIGHLIGHT_ON_INK if dark else PRIMARY
    sub = "#9AA6B5" if dark else BODY
    accent = HIGHLIGHT if dark else PRIMARY
    grid = "rgba(255,255,255,0.04)" if dark else "rgba(18,26,40,0.04)"
    panel_fill = PRIMARY if dark else MUTED
    panel_opacity = '0.35' if dark else '1'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="240" viewBox="0 0 880 240" role="img" aria-labelledby="title desc">
  <title id="title">M Ubaid Javaid — Software Engineer, Full-Stack MERN / Next.js</title>
  <desc id="desc">Professional GitHub profile header for M Ubaid Javaid, Multan, Pakistan.</desc>
  <defs>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="1.2" cy="1.2" r="0.9" fill="{grid}"/>
    </pattern>
  </defs>
  <rect width="880" height="240" rx="4" fill="{bg}"/>
  <rect width="880" height="240" rx="4" fill="url(#dots)"/>
  <rect x="0.75" y="0.75" width="878.5" height="238.5" rx="3.25" fill="none" stroke="{stroke}" stroke-width="1.5"/>
  <rect x="28" y="48" width="3" height="144" fill="{accent}"/>
  <text x="48" y="58" fill="{role}" font-family="{MONO}" font-size="12" font-weight="500" letter-spacing="1.6">SOFTWARE ENGINEER · FULL-STACK</text>
  <text x="48" y="108" fill="{name}" font-family="{FONT}" font-size="42" font-weight="700" letter-spacing="-0.8">M Ubaid Javaid</text>
  <text x="48" y="142" fill="{sub}" font-family="{FONT}" font-size="16">I engineer production web products — SaaS, fintech, healthcare, and ops platforms.</text>
  <text x="48" y="168" fill="{sub}" font-family="{FONT}" font-size="14">MERN / Next.js · Multan, Pakistan · Evolvo Technologies</text>
  <g transform="translate(48 182)">
    <g transform="scale(1.35)">{tech_mark_react()}</g>
    <g transform="translate(40 0) scale(1.35)">{tech_mark_ts()}</g>
    <g transform="translate(80 0) scale(1.35)">{tech_mark_node()}</g>
    <g transform="translate(120 0) scale(1.35)">{tech_mark_mongo()}</g>
    <g transform="translate(160 0) scale(1.35)">{tech_mark_next()}</g>
  </g>
  <g transform="translate(640 40)">
    <rect width="204" height="160" rx="14" fill="{panel_fill}" fill-opacity="{panel_opacity}" stroke="{accent}" stroke-opacity="0.5"/>
    <text x="18" y="30" fill="{role}" font-family="{MONO}" font-size="11" letter-spacing="1.4">FOCUS</text>
    {icon_cloud(18, 44, 1.15)}
    <text x="54" y="66" fill="{name}" font-family="{FONT}" font-size="14" font-weight="700">Multi-tenant SaaS</text>
    {icon_offline(18, 80, 1.15)}
    <text x="54" y="102" fill="{name}" font-family="{FONT}" font-size="14" font-weight="700">Ops dashboards</text>
    {icon_shield(18, 116, 1.15)}
    <text x="54" y="138" fill="{name}" font-family="{FONT}" font-size="14" font-weight="700">API architecture</text>
  </g>
</svg>'''


def divider(dark: bool) -> str:
    stroke = "#1C2636" if dark else BORDER
    accent = HIGHLIGHT if dark else PRIMARY
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="28" viewBox="0 0 880 28" role="presentation" aria-hidden="true">
  <line x1="0" y1="14" x2="392" y2="14" stroke="{stroke}" stroke-width="1"/>
  <circle cx="440" cy="14" r="5" fill="{accent}"/>
  <circle cx="440" cy="14" r="2" fill="{SURFACE if not dark else INK_DEEP}"/>
  <line x1="488" y1="14" x2="880" y2="14" stroke="{stroke}" stroke-width="1"/>
</svg>'''


def kicker(label: str, filename: str, icon_fn) -> None:
    # 48 well centered in 64; icon 24@1.5=36 → pad 6
    write(
        f"kickers/{filename}",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="64" viewBox="0 0 880 64" role="img" aria-label="{label}">
  <rect x="0" y="8" width="48" height="48" rx="14" fill="{MUTED}" stroke="{BORDER}"/>
  {icon_fn(6, 14, 1.5)}
  <text x="64" y="40" fill="{PRIMARY}" font-family="{MONO}" font-size="16" font-weight="700" letter-spacing="2.6">{label.upper()}</text>
</svg>''',
    )


def button(label: str, filename: str, icon_fn, filled: bool = False) -> None:
    """Icon well + text optically centered — fixes navy-on-navy portfolio globe."""
    h, w = 60, 210
    well, well_x, well_y = 36, 12, 12  # (60-36)/2 = 12
    icon_pad = 6  # (36 - 24*1.0)/2 when s=1.0 → use 1.0 then pad; use s=1.0 with pad 6 for crisp
    # Prefer slightly larger: s=1.1 → 26.4, pad=(36-26.4)/2=4.8
    icon_s = 1.1
    icon_pad = round((well - 24 * icon_s) / 2, 1)
    fill = PRIMARY if filled else SURFACE
    stroke = PRIMARY
    text = PAPER if filled else INK
    well_fill = "rgba(255,255,255,0.18)" if filled else MUTED
    well_stroke = "rgba(255,255,255,0.35)" if filled else BORDER
    # Portfolio filled uses light globe so strokes stay visible on navy well
    ix, iy = well_x + icon_pad, well_y + icon_pad
    icon_svg = icon_fn(ix, iy, icon_s)
    if filled and filename == "btn-portfolio.svg":
        icon_svg = icon_globe(ix, iy, icon_s, "#79B4E8")
    text_x = well_x + well + 14
    text_y = h // 2 + 6  # optical center for ~16px bold
    write(
        f"buttons/{filename}",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">
  <defs>
    <linearGradient id="btnGrad{filename.replace('.', '')}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{PRIMARY if filled else SURFACE}"/>
      <stop offset="100%" stop-color="{HIGHLIGHT if filled else MUTED}"/>
    </linearGradient>
  </defs>
  <rect x="0.75" y="0.75" width="{w - 1.5}" height="{h - 1.5}" rx="14" fill="{"url(#btnGrad" + filename.replace('.', '') + ")" if filled else SURFACE}" stroke="{stroke}" stroke-width="2"/>
  <rect x="{well_x}" y="{well_y}" width="{well}" height="{well}" rx="10" fill="{well_fill}" stroke="{well_stroke}"/>
  {icon_svg}
  <text x="{text_x}" y="{text_y:.0f}" fill="{text}" font-family="{FONT}" font-size="16" font-weight="700">{label}</text>
</svg>''',
    )


STRIP_BG = ["#EFF6FF", "#F5F3FF", "#FDF2F8", "#ECFDF5", "#FFFBEB", "#F0F9FF"]
STRIP_WELL = ["#DBEAFE", "#EDE9FE", "#FCE7F3", "#D1FAE5", "#FEF3C7", "#E0F2FE"]


def strip(title: str, items: list[tuple[str, str, str]], filename: str, height: int = 176) -> None:
    """items: (headline, sub, icon_svg_at_origin) — icon in a centered well, text block aligned."""
    n = len(items)
    gap = 14
    pad = 20
    usable = 880 - pad * 2 - gap * (n - 1)
    w = usable / n
    card_y, card_h = 48, 112
    well = 44
    cards = []
    for i, (h, sub, ic) in enumerate(items):
        x = pad + i * (w + gap)
        bg = STRIP_BG[i % len(STRIP_BG)]
        well_bg = STRIP_WELL[i % len(STRIP_WELL)]
        well_x = x + 14
        well_y = card_y + (card_h - well) / 2
        # icon 24 @ 1.25 = 30 → pad (44-30)/2 = 7
        icon_s = 1.25
        icon_pad = (well - 24 * icon_s) / 2
        text_x = well_x + well + 12
        title_y = well_y + 18
        sub_y = well_y + 40
        cards.append(
            f'''  <rect x="{x:.1f}" y="{card_y}" width="{w:.1f}" height="{card_h}" rx="16" fill="{bg}" stroke="{BORDER}"/>
  <rect x="{well_x:.1f}" y="{well_y:.1f}" width="{well}" height="{well}" rx="12" fill="{well_bg}" stroke="{BORDER}"/>
  <g transform="translate({well_x + icon_pad:.1f} {well_y + icon_pad:.1f}) scale({icon_s})">{ic}</g>
  <text x="{text_x:.1f}" y="{title_y:.1f}" fill="{INK}" font-family="{FONT}" font-size="15" font-weight="700">{h}</text>
  <text x="{text_x:.1f}" y="{sub_y:.1f}" fill="{BODY}" font-family="{FONT}" font-size="12">{sub}</text>'''
        )
    write(
        filename,
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="{height}" viewBox="0 0 880 {height}" role="img" aria-labelledby="t">
  <title id="t">{title}</title>
  <rect width="880" height="{height}" rx="10" fill="{SURFACE}" stroke="{BORDER}"/>
  <text x="20" y="30" fill="{PRIMARY}" font-family="{MONO}" font-size="12" letter-spacing="1.8">{title.upper()}</text>
{chr(10).join(cards)}
</svg>''',
    )


def card(code: str, title: str, blurb: list[str], meta: str, filename: str, accent: str, icon_fn) -> None:
    tspans = "\n".join(
        f'    <tspan x="24" dy="{"0" if i == 0 else "18"}">{line}</tspan>'
        for i, line in enumerate(blurb)
    )
    write(
        f"cards/{filename}",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="520" height="268" viewBox="0 0 520 268" role="img" aria-labelledby="t">
  <title id="t">{code} — {title}</title>
  <defs>
    <linearGradient id="g{code}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="{SURFACE}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect x="0.75" y="0.75" width="518.5" height="266.5" rx="14" fill="{SURFACE}" stroke="{BORDER}" stroke-width="1.5"/>
  <rect x="0.75" y="0.75" width="518.5" height="266.5" rx="14" fill="url(#g{code})"/>
  <rect x="0" y="0" width="8" height="268" fill="{accent}"/>
  <text x="24" y="42" fill="{accent}" font-family="{MONO}" font-size="13" font-weight="700" letter-spacing="1.8">{code}</text>
  <text x="24" y="80" fill="{INK}" font-family="{FONT}" font-size="24" font-weight="700">{title}</text>
  <text x="24" y="108" fill="{BODY}" font-family="{FONT}" font-size="13">{meta}</text>
  <text x="24" y="144" fill="{BODY}" font-family="{FONT}" font-size="14">
{tspans}
  </text>
  <text x="24" y="240" fill="{accent}" font-family="{FONT}" font-size="14" font-weight="700">Case study →</text>
  <rect x="318" y="28" width="180" height="180" rx="24" fill="{MUTED}" stroke="{accent}" stroke-width="2.5" stroke-opacity="0.5"/>
  {icon_fn(346, 56, 5.1)}
</svg>''',
    )


def github_progress() -> str:
    """Verified portfolio progress + creative activity board (not fake commit counts)."""
    rows = [
        ("Case studies documented", 6, 6, "#0D9488", "#CCFBF1", icon_policy),
        ("Verified engineering roles", 2, 2, "#7C3AED", "#EDE9FE", icon_briefcase),
        ("Featured production systems", 6, 6, "#0369A1", "#E0F2FE", icon_cloud),
        ("Public portfolio + writing", 4, 4, "#DB2777", "#FCE7F3", icon_globe),
    ]
    parts = []
    for i, (label, done, total, color, well, ic) in enumerate(rows):
        y = 62 + i * 54
        bar_w = 620 * (done / total)
        # 40px well, icon 24@1.25=30 → pad 5
        parts.append(
            f'''  <rect x="24" y="{y}" width="832" height="48" rx="14" fill="{MUTED}"/>
  <rect x="34" y="{y + 4}" width="40" height="40" rx="12" fill="{well}" stroke="{color}" stroke-opacity="0.35"/>
  {ic(39, y + 9, 1.25)}
  <text x="90" y="{y + 20}" fill="{INK}" font-family="{FONT}" font-size="14" font-weight="700">{label}</text>
  <text x="832" y="{y + 20}" text-anchor="end" fill="{color}" font-family="{MONO}" font-size="13" font-weight="700">{done}/{total}</text>
  <rect x="90" y="{y + 30}" width="620" height="10" rx="5" fill="#E2E8F0"/>
  <rect x="90" y="{y + 30}" width="{bar_w:.0f}" height="10" rx="5" fill="{color}"/>
  <circle cx="{90 + bar_w:.0f}" cy="{y + 35}" r="5" fill="{SURFACE}" stroke="{color}" stroke-width="2"/>'''
        )

    cells = []
    levels = [
        0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 2, 3, 4, 3, 1, 0, 1, 3, 4, 4, 3, 2, 1,
        0, 1, 2, 3, 2, 0, 0, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 2, 1, 0, 0, 1, 3, 4, 3, 2, 1,
        1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 4, 3, 2, 1, 0, 2, 3, 4, 2, 1, 0, 1, 2, 3, 4, 3, 1, 0,
    ]
    palette = ["#E2E8F0", "#99F6E4", "#67E8F9", "#60A5FA", "#2A527A", "#A78BFA", "#F472B6"]
    # Remap 0-4 into richer palette indices for more color
    remap = [0, 1, 2, 3, 4, 5, 6]
    for i, lv in enumerate(levels[:84]):
        col = i % 28
        row = i // 28
        tone = remap[lv % len(remap)] if lv else 0
        if lv >= 3:
            tone = 3 + (i % 4)  # mix blues/violets/pinks on hot cells
            tone = min(tone, 6)
        cells.append(
            f'<rect x="{28 + col * 30}" y="{298 + row * 28}" width="24" height="24" rx="6" fill="{palette[tone]}"/>'
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="420" viewBox="0 0 880 420" role="img" aria-labelledby="t d">
  <title id="t">Engineering progress and craft rhythm</title>
  <desc id="d">Verified portfolio progress bars plus an illustrative craft-rhythm board. Not a live GitHub contribution graph.</desc>
  <defs>
    <linearGradient id="gpHead" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#2A527A"/>
      <stop offset="55%" stop-color="#3878B0"/>
      <stop offset="100%" stop-color="#0D9488"/>
    </linearGradient>
  </defs>
  <rect width="880" height="420" rx="14" fill="{SURFACE}" stroke="{BORDER}"/>
  <rect width="880" height="52" rx="14" fill="url(#gpHead)"/>
  <rect y="26" width="880" height="26" fill="url(#gpHead)"/>
  {icon_github(24, 12, 1.15)}
  <text x="60" y="34" fill="#F4F7FA" font-family="{FONT}" font-size="18" font-weight="700">GitHub profile progress</text>
  <text x="852" y="34" text-anchor="end" fill="#DBEAFE" font-family="{MONO}" font-size="11">VERIFIED · PORTFOLIO</text>
{chr(10).join(parts)}
  <text x="28" y="286" fill="{PRIMARY}" font-family="{MONO}" font-size="11" letter-spacing="1.4">CRAFT RHYTHM · ILLUSTRATIVE PATTERN</text>
{chr(10).join(cells)}
  <text x="28" y="408" fill="{BODY}" font-family="{FONT}" font-size="11">Bars match published case studies, roles, and portfolio surfaces — not invented commit totals.</text>
</svg>'''


def github_overview() -> str:
    """Local GitHub overview card — no third-party image host."""
    facts = [
        ("6", "Case studies", "#0D9488", icon_policy),
        ("2", "Verified roles", "#7C3AED", icon_briefcase),
        ("6", "Live systems", "#0369A1", icon_cloud),
        ("3", "Public essays", "#DB2777", icon_globe),
    ]
    tiles = []
    for i, (num, label, color, ic) in enumerate(facts):
        col = i % 2
        row = i // 2
        x = 24 + col * 200
        y = 72 + row * 72
        tiles.append(
            f'''  <rect x="{x}" y="{y}" width="188" height="60" rx="12" fill="{MUTED}"/>
  <rect x="{x + 10}" y="{y + 10}" width="40" height="40" rx="10" fill="{SURFACE}" stroke="{color}" stroke-opacity="0.4"/>
  {ic(x + 18, y + 18, 1.0)}
  <text x="{x + 62}" y="{y + 28}" fill="{color}" font-family="{MONO}" font-size="20" font-weight="700">{num}</text>
  <text x="{x + 62}" y="{y + 48}" fill="{BODY}" font-family="{FONT}" font-size="12">{label}</text>'''
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="424" height="220" viewBox="0 0 424 220" role="img" aria-labelledby="t">
  <title id="t">GitHub profile overview — verified portfolio evidence</title>
  <defs>
    <linearGradient id="goHead" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#181717"/>
      <stop offset="100%" stop-color="#2A527A"/>
    </linearGradient>
  </defs>
  <rect width="424" height="220" rx="14" fill="{SURFACE}" stroke="{BORDER}"/>
  <rect width="424" height="52" rx="14" fill="url(#goHead)"/>
  <rect y="26" width="424" height="26" fill="url(#goHead)"/>
  {icon_github(18, 12, 1.15)}
  <text x="54" y="34" fill="#F4F7FA" font-family="{FONT}" font-size="16" font-weight="700">dev-mubaidjavaid</text>
  <text x="400" y="34" text-anchor="end" fill="#A7F3D0" font-family="{MONO}" font-size="10">LOCAL · ALWAYS LOADS</text>
{chr(10).join(tiles)}
</svg>'''


def github_langs() -> str:
    """Primary craft languages from shipping work — not invented GitHub percentages."""
    langs = [
        ("TypeScript", 0.92, C_TS),
        ("JavaScript", 0.78, "#EAB308"),
        ("CSS / Tailwind", 0.70, C_TAIL),
        ("Node / Express", 0.66, C_NODE),
        ("Python tooling", 0.42, "#3776AB"),
    ]
    bars = []
    for i, (name, pct, color) in enumerate(langs):
        y = 64 + i * 28
        bw = 280 * pct
        bars.append(
            f'''  <text x="24" y="{y + 12}" fill="{INK}" font-family="{FONT}" font-size="13" font-weight="600">{name}</text>
  <rect x="150" y="{y}" width="250" height="14" rx="7" fill="#E2E8F0"/>
  <rect x="150" y="{y}" width="{bw:.0f}" height="14" rx="7" fill="{color}"/>
  <text x="410" y="{y + 12}" text-anchor="end" fill="{BODY}" font-family="{MONO}" font-size="11">{int(pct * 100)}</text>'''
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="424" height="220" viewBox="0 0 424 220" role="img" aria-labelledby="t">
  <title id="t">Primary languages in shipping work</title>
  <rect width="424" height="220" rx="14" fill="{SURFACE}" stroke="{BORDER}"/>
  <rect width="424" height="52" rx="14" fill="{PRIMARY}"/>
  <rect y="26" width="424" height="26" fill="{PRIMARY}"/>
  {icon_config(18, 12, 1.15)}
  <text x="54" y="34" fill="#F4F7FA" font-family="{FONT}" font-size="16" font-weight="700">Craft languages</text>
  <text x="400" y="34" text-anchor="end" fill="#DBEAFE" font-family="{MONO}" font-size="10">PORTFOLIO EMPHASIS</text>
{chr(10).join(bars)}
  <text x="24" y="208" fill="{BODY}" font-family="{FONT}" font-size="10">Relative emphasis in published work — not live GitHub API shares.</text>
</svg>'''


def architecture() -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="330" viewBox="0 0 880 330" role="img" aria-labelledby="t d">
  <title id="t">Production system architecture</title>
  <desc id="d">Clients to edge app to API and rules to data, with tenant isolation, offline queue, and config-as-data.</desc>
  <rect width="880" height="330" rx="4" fill="{SURFACE}" stroke="{BORDER}"/>
  <text x="28" y="36" fill="{INK}" font-family="{FONT}" font-size="16" font-weight="700">Production system shape</text>
  <text x="28" y="56" fill="{BODY}" font-family="{FONT}" font-size="12">How HSMS / QuikPOS-class platforms are layered in practice</text>

  <rect x="28" y="78" width="170" height="100" rx="10" fill="#EFF6FF" stroke="{PRIMARY}"/>
  {icon_users(90, 88, 1.1)}
  <text x="113" y="148" text-anchor="middle" fill="{PRIMARY}" font-family="{FONT}" font-size="14" font-weight="700">Clients</text>
  <text x="113" y="166" text-anchor="middle" fill="{BODY}" font-family="{FONT}" font-size="11">Web · PWA · Admin</text>

  <text x="214" y="132" fill="{BORDER}" font-size="20">→</text>

  <rect x="238" y="78" width="170" height="100" rx="10" fill="#F0FDFA" stroke="#0D9488"/>
  {icon_cloud(300, 88, 1.1)}
  <text x="323" y="148" text-anchor="middle" fill="#0F766E" font-family="{FONT}" font-size="14" font-weight="700">Edge / App</text>
  <text x="323" y="166" text-anchor="middle" fill="{BODY}" font-family="{FONT}" font-size="11">Next.js · Auth · RBAC</text>

  <text x="424" y="132" fill="{BORDER}" font-size="20">→</text>

  <rect x="448" y="78" width="170" height="100" rx="10" fill="#EEF2FF" stroke="#6366F1"/>
  {icon_shield(510, 88, 1.1)}
  <text x="533" y="148" text-anchor="middle" fill="#4338CA" font-family="{FONT}" font-size="14" font-weight="700">API / Rules</text>
  <text x="533" y="166" text-anchor="middle" fill="{BODY}" font-family="{FONT}" font-size="11">Express · Security rules</text>

  <text x="634" y="132" fill="{BORDER}" font-size="20">→</text>

  <rect x="658" y="78" width="190" height="100" rx="10" fill="#F0FDF4" stroke="#16A34A"/>
  {icon_db(733, 88, 1.1)}
  <text x="753" y="148" text-anchor="middle" fill="#166534" font-family="{FONT}" font-size="14" font-weight="700">Data</text>
  <text x="753" y="166" text-anchor="middle" fill="{BODY}" font-family="{FONT}" font-size="11">MongoDB · Firestore · Convex</text>

  <rect x="28" y="214" width="260" height="84" rx="10" fill="#FFFBEB" stroke="#D97706"/>
  {icon_tenant(48, 236, 1)}
  <text x="88" y="252" fill="#92400E" font-family="{FONT}" font-size="14" font-weight="700">Tenant isolation</text>
  <text x="88" y="274" fill="{BODY}" font-family="{FONT}" font-size="12">Platform-enforced — not ad-hoc filters</text>

  <rect x="308" y="214" width="260" height="84" rx="10" fill="#EEF2FF" stroke="#6366F1"/>
  {icon_offline(328, 236, 1)}
  <text x="368" y="252" fill="#3730A3" font-family="{FONT}" font-size="14" font-weight="700">Offline queue</text>
  <text x="368" y="274" fill="{BODY}" font-family="{FONT}" font-size="12">IndexedDB → reconcile on reconnect</text>

  <rect x="588" y="214" width="260" height="84" rx="10" fill="#FEF3C7" stroke="#F59E0B"/>
  {icon_config(608, 236, 1)}
  <text x="648" y="252" fill="#92400E" font-family="{FONT}" font-size="14" font-weight="700">Config as data</text>
  <text x="648" y="274" fill="{BODY}" font-family="{FONT}" font-size="12">Workflows &amp; forms without redeploy</text>
</svg>'''


def auth_flow() -> str:
    steps = [
        ("Auth", "JWT / session", icon_key),
        ("Role", "RBAC claims", icon_role),
        ("Tenant", "Scope boundary", icon_tenant),
        ("Policy", "ABAC rules", icon_policy),
        ("Action", "Persisted write", icon_action),
    ]
    parts = []
    colors = ["#FFFBEB", "#F5F3FF", "#F0FDFA", "#EFF6FF", "#F0FDF4"]
    strokes = ["#D97706", "#8B5CF6", "#0D9488", "#2563EB", "#16A34A"]
    for i, ((h, s, ic), bg, st) in enumerate(zip(steps, colors, strokes)):
        x = 28 + i * 168
        parts.append(
            f'''  <rect x="{x}" y="68" width="148" height="90" rx="10" fill="{bg}" stroke="{st}"/>
  {ic(x + 62, 78, 0.95)}
  <text x="{x + 74}" y="128" text-anchor="middle" fill="{INK}" font-family="{FONT}" font-size="14" font-weight="700">{h}</text>
  <text x="{x + 74}" y="146" text-anchor="middle" fill="{BODY}" font-family="{FONT}" font-size="11">{s}</text>'''
        )
        if i < 4:
            parts.append(f'  <text x="{x + 154}" y="118" fill="{BORDER}" font-size="16">→</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="190" viewBox="0 0 880 190" role="img" aria-labelledby="t">
  <title id="t">Auth to role to tenant to policy to action</title>
  <rect width="880" height="190" rx="4" fill="{SURFACE}" stroke="{BORDER}"/>
  <text x="28" y="36" fill="{INK}" font-family="{FONT}" font-size="15" font-weight="700">Authorization path</text>
  <text x="28" y="54" fill="{BODY}" font-family="{FONT}" font-size="12">From identity to a permitted, tenant-scoped write</text>
{chr(10).join(parts)}
</svg>'''


def delivery() -> str:
    steps = [
        ("Model", "#0EA5E9", icon_db),
        ("Slice", "#8B5CF6", icon_offline),
        ("Harden", "#2563EB", icon_shield),
        ("Ship", "#D97706", icon_cloud),
        ("Live", "#16A34A", icon_action),
    ]
    parts = []
    for i, (s, c, ic) in enumerate(steps):
        x = 40 + i * 160
        parts.append(
            f'''  <circle cx="{x + 40}" cy="108" r="34" fill="{c}" fill-opacity="0.15" stroke="{c}" stroke-width="2"/>
  {ic(x + 28, 96, 1)}
  <text x="{x + 40}" y="162" text-anchor="middle" fill="{INK}" font-family="{FONT}" font-size="13" font-weight="700">{s}</text>
  <text x="{x + 40}" y="178" text-anchor="middle" fill="{BODY}" font-family="{MONO}" font-size="11">0{i + 1}</text>'''
        )
        if i < 4:
            parts.append(
                f'  <line x1="{x + 78}" y1="108" x2="{x + 122}" y2="108" stroke="{c}" stroke-width="2" stroke-dasharray="4 3"/>'
            )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="200" viewBox="0 0 880 200" role="img" aria-labelledby="t">
  <title id="t">Delivery loop: model, slice, harden, ship, live</title>
  <rect width="880" height="200" rx="4" fill="{SURFACE}" stroke="{BORDER}"/>
  <text x="28" y="36" fill="{INK}" font-family="{FONT}" font-size="15" font-weight="700">Delivery loop</text>
  <text x="28" y="54" fill="{BODY}" font-family="{FONT}" font-size="12">Vertical slices over half-built feature sprawl</text>
{chr(10).join(parts)}
</svg>'''


def stack_visual() -> str:
    badges = [
        (16, 48, "React", tech_mark_react(), "#E0F2FE"),
        (94, 48, "TypeScript", tech_mark_ts(), "#DBEAFE"),
        (172, 48, "Next.js", tech_mark_next(), "#F1F5F9"),
        (250, 48, "Node.js", tech_mark_node(), "#DCFCE7"),
        (328, 48, "Express", tech_mark_express(), "#F3F4F6"),
        (406, 48, "MongoDB", tech_mark_mongo(), "#DCFCE7"),
        (484, 48, "Firebase", tech_mark_firebase(), "#FEF3C7"),
        (562, 48, "Tailwind", tech_mark_tailwind(), "#CFFAFE"),
        (640, 48, "Docker", tech_mark_docker(), "#E0F2FE"),
        (718, 48, "Vercel", tech_mark_vercel(), "#F1F5F9"),
        (796, 48, "Git", tech_mark_git(), "#FEE2E2"),
    ]
    parts = []
    for x, y, name, mark, bg in badges:
        parts.append(
            f'''  <g transform="translate({x} {y})">
    <rect width="72" height="96" rx="14" fill="{bg}" stroke="{BORDER}"/>
    <g transform="translate(16 14) scale(1.65)">{mark}</g>
    <text x="36" y="82" text-anchor="middle" fill="{INK}" font-family="{FONT}" font-size="11" font-weight="700">{name}</text>
  </g>'''
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="170" viewBox="0 0 880 170" role="img" aria-labelledby="t">
  <title id="t">Technology stack with brand icons</title>
  <rect width="880" height="170" rx="8" fill="{SURFACE}" stroke="{BORDER}"/>
  <text x="20" y="28" fill="{PRIMARY}" font-family="{MONO}" font-size="12" letter-spacing="1.8">STACK — LARGE COLOR ICONS</text>
{chr(10).join(parts)}
</svg>'''


def main() -> None:
    write("hero-dark.svg", hero(True))
    write("hero-light.svg", hero(False))
    write("divider.svg", divider(False))
    write("divider-dark.svg", divider(True))

    kicker("Selected work", "kicker-work.svg", lambda x, y, s: icon_briefcase(x, y, s))
    kicker("Evolvo delivery", "kicker-evolvo.svg", lambda x, y, s: icon_cloud(x, y, s, "#0EA5E9"))
    kicker("Stack", "kicker-stack.svg", lambda x, y, s: icon_config(x, y, s))
    kicker("Experience", "kicker-system.svg", lambda x, y, s: icon_briefcase(x, y, s))
    kicker("How I work", "kicker-signal.svg", lambda x, y, s: icon_shield(x, y, s))
    kicker("Writing", "kicker-writing.svg", lambda x, y, s: icon_policy(x, y, s))

    button("Portfolio", "btn-portfolio.svg", icon_globe, filled=True)
    button("Case studies", "btn-cases.svg", icon_briefcase)
    button("LinkedIn", "btn-linkedin.svg", icon_linkedin)
    button("Email", "btn-email.svg", icon_mail)
    button("GitHub", "btn-github.svg", icon_github)

    strip(
        "Domains",
        [
            ("Fintech", "Payments · portals", icon_fintech(0, 0, 1)),
            ("Healthcare", "Ops · clinic surfaces", icon_health(0, 0, 1)),
            ("Ops / POS", "Multi-tenant retail", icon_pos(0, 0, 1)),
            ("Commerce", "D2C storefronts", icon_bag(0, 0, 1)),
        ],
        "domains-strip.svg",
    )
    strip(
        "Evidence — not invented metrics",
        [
            ("6", "Written case studies", icon_policy(0, 0, 1)),
            ("2", "Verified roles", icon_briefcase(0, 0, 1)),
            ("50+", "Evolvo sites attributed", icon_cloud(0, 0, 1)),
            ("0", "Invented testimonials", icon_action(0, 0, 1)),
        ],
        "proof-strip.svg",
    )
    write("stack-strip.svg", stack_visual())
    strip(
        "Experience",
        [
            ("Evolvo Technologies", "Feb 2026 – present", icon_cloud(0, 0, 1)),
            ("Fiesta Content Solutions", "Jul 2024 – Jan 2026", icon_briefcase(0, 0, 1)),
        ],
        "experience-strip.svg",
        height=176,
    )
    strip(
        "Writing",
        [
            ("Next.js vs SPA", "Business websites", icon_globe(0, 0, 1, "#111111")),
            ("Vercel vs VPS", "SaaS hosting", icon_cloud(0, 0, 1)),
            ("Hiring Next.js", "Pakistan freelancers", icon_users(0, 0, 1)),
        ],
        "writing-strip.svg",
    )
    strip(
        "Contact",
        [
            ("Email", "mubaidjavaid97@gmail.com", icon_mail(0, 0, 1)),
            ("Portfolio", "mubaidjavaid.vercel.app", icon_globe(0, 0, 1)),
            ("LinkedIn", "m-ubaid-javaid", icon_linkedin(0, 0, 1)),
        ],
        "contact-strip.svg",
    )

    card("HSMS", "Housing Society OS",
         ["Metadata-driven workflows, plot lifecycle,", "installment billing, compliance surfaces."],
         "Multi-tenant · RBAC+ABAC · Offline PWA", "card-hsms.svg", "#0D9488",
         lambda x, y, s: icon_building(x, y, s))
    card("QUIKPOS", "Point-of-Sale SaaS",
         ["Tenant-isolated POS with credit ledgers,", "barcode flows, and offline reconciliation."],
         "React · Vite · Firebase · Zustand", "card-pos.svg", "#7C3AED",
         lambda x, y, s: icon_pos(x, y, s))
    card("NAAZ", "D2C E-Commerce",
         ["Catalog, checkout, tracking, admin, and", "receipts — SSR pages with Convex backends."],
         "Next.js · Convex · Cloudinary · PWA", "card-commerce.svg", "#DB2777",
         lambda x, y, s: icon_bag(x, y, s))
    card("APEX", "Fintech Platform",
         ["Institutional portal: payments, multicurrency,", "custody visualisation, SSR + dashboard."],
         "Next.js · TypeScript · Three.js · GSAP", "card-fintech.svg", "#0369A1",
         lambda x, y, s: icon_fintech(x, y, s))
    card("SURGI", "Surgical Ops",
         ["Surgical management surfaces delivered", "as Evolvo client production work."],
         "Evolvo delivery · Live product", "card-surgicore.svg", "#059669",
         lambda x, y, s: icon_surgery(x, y, s))
    card("VITALIS", "Healthcare Platform",
         ["Clinic and admin surfaces shipped for", "healthcare operations — Evolvo delivery."],
         "Evolvo delivery · Live product", "card-vitalis.svg", "#E11D48",
         lambda x, y, s: icon_health(x, y, s))

    write("diagrams/architecture.svg", architecture())
    write("diagrams/auth-flow.svg", auth_flow())
    write("diagrams/delivery.svg", delivery())
    write("github-progress.svg", github_progress())
    write("github-overview.svg", github_overview())
    write("github-langs.svg", github_langs())
    print("done")


if __name__ == "__main__":
    main()

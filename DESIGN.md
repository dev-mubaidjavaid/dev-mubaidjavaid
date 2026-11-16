---
name: M Ubaid Javaid Portfolio
description: Cool paper + ink editorial portfolio with a single steel-navy accent family
colors:
  paper: "#F4F7FA"
  ink: "#121A28"
  ink-deep: "#080A10"
  body: "#566374"
  muted-surface: "#EEF2F6"
  border: "#D8E0EA"
  primary: "#2A527A"
  primary-hover: "#234568"
  highlight: "#3878B0"
  highlight-soft: "#7AAFDB"
  highlight-on-ink: "#79B4E8"
  surface-elevated: "#FFFFFF"
  destructive: "#D12B2B"
typography:
  display:
    fontFamily: "Syne, system-ui, sans-serif"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.025em"
  body:
    fontFamily: "Plus Jakarta Sans, system-ui, sans-serif"
    fontWeight: 400
    lineHeight: 1.75
  mono:
    fontFamily: "IBM Plex Mono, ui-monospace, monospace"
    fontSize: "0.75rem"
    fontWeight: 500
    letterSpacing: "0.04em"
rounded:
  sm: "0px"
  md: "2px"
  lg: "0.125rem"
spacing:
  rail-x: "24px–48px"
  rail-y: "64px–96px"
  section-y: "96px–160px"
  container: "1180px"
components:
  cta-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.paper}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
  cta-primary-hover:
    backgroundColor: "{colors.primary-hover}"
  cta-primary-ink:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
---

# Design System

## Overview

An editorial product-engineer portfolio on cool paper surfaces with deep ink heroes. One accent family only — steel navy (`hsl(211 …)`) — never purple, neon, or multi-gradient CTA kits. Homepage sections follow a strict composition grammar: **BrandSection + BrandCopy + BrandStage**, with the stage holding exactly one media type (`product` | `diagram` | `motion` | `code`).

Visitor mode on the homepage and marketing surfaces: **Experience / Persuade** — the person and work lead; chrome stays quiet.

Authoritative code sources: `lib/brand-system.ts`, `app/globals.css`, `tailwind.config.ts`, `app/layout.tsx` (fonts).

## Colors

| Role | Token / usage | Notes |
|------|---------------|--------|
| Paper | `--background` / `paper` | Cool off-white page field |
| Ink | `--heading` / `ink` | Display + strong UI text |
| Ink deep | `#06080F` hero field | Full-bleed ink stages only |
| Body | `--body` | Long-form / lead copy |
| Primary | `--primary` | CTAs only |
| Highlight | `--highlight` | Labels, mono accents |
| Highlight on ink | `--highlight-on-ink` | Labels on dark stages |
| Border | `--border` | Hairlines; keep low contrast |

**Do not** invent secondary accent hues. Prefer Tailwind semantic classes (`bg-primary`, `text-highlight`, `text-heading`) over raw hex except for the approved ink-deep hero field until it is tokenized as `--ink-deep`.

Approximate hex above maps from HSL CSS variables for DESIGN.md portability; runtime source of truth remains `hsl(var(--…))` in CSS.

## Typography

- **Display / headings:** Syne (`--font-display`) — bold, tight tracking, fluid clamps via `brandType` / CSS fluid scale
- **Body:** Plus Jakarta Sans (`--font-body`) — product-legible, not Inter/system default
- **Meta / labels:** IBM Plex Mono (`--font-mono`) + `.section-label` / `brandType.label`
- Headings use `text-balance` where applied; body line length targets ~55–70ch on leads (`max-w-md` / `max-w-xl`)
- Numeric proof: `.tabular-nums-pro`

## Layout

- Grid: 12 columns, `max-w-[1180px]` (`.container-wide`)
- Split: copy **5/12** · stage **7/12** (stage visual majority); reverse allowed
- Band: full-bleed stage with copy rail
- Safe areas: horizontal padding uses `env(safe-area-inset-*)`
- Mobile: bottom nav clearance on `body` (`pb-[calc(3.5rem+safe-area)]`)
- Hero budget (homepage): brand/role signal, one headline, one supporting sentence, CTA group, one dominant visual plane — no first-viewport card grids or stat strips

ASCII (homepage split):

```
| copy 5/12              | stage 7/12                 |
| label                  | product | diagram |        |
| title                  | motion  | code             |
| lead + CTA             |                          |
```

## Elevation & Depth

- Prefer flat paper / muted / ink stage tones over stacked card chrome
- Soft shadows only where interaction needs lift; avoid identical SaaS card shadows on every block
- Ink stages may use restrained radial dots + single steel bloom — not purple glow kits

## Shapes

- Radius is intentionally sharp: `--radius: 0.125rem` (near hairline product UI)
- CTAs: rectangular (`.cta-primary`), not pill clusters
- Borders: hairline `border-border/…`

## Components

- **CTA:** `.cta-primary` / `.cta-primary-ink` — min height 44px (`min-h-11`)
- **Button primitive:** `components/ui/button.tsx` — `focus-visible` ring required
- **Brand section shell:** `components/brand/system/*`
- **Diagrams:** `NetworkGraph` (systems) · `WorkflowPath` (process only)
- **Approved Lottie roles only:** craft / write / connect (`brandMotionRole`)
- **Motion curves:** `brandMotion.ease = [0.22, 1, 0.36, 1]`; UI micro ≤ ~300–600ms; compositor props only

## Do's and Don'ts

**Do**
- Map color/spacing/type to tokens and `brandSpace` / `brandType`
- Keep one media type per stage
- Honor `prefers-reduced-motion` for Lenis, Lottie, CSS loops, and scroll reveals
- Use real project imagery in Selected Work / Impact

**Don't**
- Add purple/cyan accent drift or multi-stop CTA gradients
- Reintroduce orbit / ring / ad-hoc SVG languages outside approved diagrams
- Animate `width` / `height` / `top` / `left` / `margin`
- Ship `transition-all` or `outline-none` without a `:focus-visible` replacement
- Leave parallel “legacy section” visual systems competing with Brand* on the homepage

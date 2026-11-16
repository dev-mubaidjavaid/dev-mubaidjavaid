# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary: founders, product leads, and hiring managers evaluating a remote-capable software engineer for MERN / Next.js product work (fintech, healthcare, SaaS).

Secondary: peers and clients seeking proof of delivery quality via case studies and writing.

## Product Purpose

Personal portfolio and lead-conversion site for **M Ubaid Javaid** — Software Engineer (full-stack MERN / Next.js) based in Multan, Pakistan. Success = visitors understand capability quickly, trust production evidence, and start a contact / discovery conversation.

## Positioning

Not a generic “developer portfolio kit.” Positions as **engineering with product judgment**: architecture-first delivery, conversion-aware interfaces, and end-to-end ownership across Evolvo client work (fintech, healthcare, prop trading, real estate) plus prior MERN product experience.

## Capabilities

- Homepage brand narrative (hero → fit → proof → impact → process → stack → timeline → writing → contact)
- Work / project case pages with media
- Blog / writing
- Services
- About
- Contact form (API + validation) and discovery-call modal
- SEO (metadata, sitemap, robots, JSON-LD)

## Constraints

- Stack is Next.js 16 App Router, React 19, Tailwind 3, TypeScript
- Motion stack includes Framer Motion, GSAP (`@gsap/react`), and Lenis
- Brand system documented in `lib/brand-system.ts` + CSS tokens in `app/globals.css`
- Light theme is the shipped default (`html` locked to `light`; `colorScheme: light`)
- Must remain malware-clean; no risky editor auto-tasks or obfuscated config payloads

## Voice

Confident, specific, active. Prefer outcome language over buzzwords. Avoid placeholder / lorem copy.

## Evidence (repo)

- Canonical copy & nav: `data/site.ts`
- Brand composition rules: `lib/brand-system.ts`
- Routes: `/`, `/projects`, `/projects/[slug]`, `/blog`, `/blog/[slug]`, `/about`, `/services`, `/contact`, `/contact/thank-you`
- Contact: `app/api/contact`, `lib/contact-schema.ts`

## Open decisions

- [inferred] Whether dark mode should be fully shipped or ThemeToggle / ThemeProvider should be removed as dead UI
- [inferred] Whether legacy `components/sections/*` (orbits, older heroes) should be deleted or kept only for non-home pages
- [confirm] Target ICP priority: freelance clients vs full-time employers vs Evolvo-adjacent leads

## Accessibility

Target WCAG AA for marketing/portfolio surfaces: keyboard access, visible focus, reduced motion, meaningful image text, labeled forms.

# Agency Swarm Landing Page — Design Spec

Run anchor: `20260420T210900Z`  
Source issue: [PORAAA-9](/PORAAA/issues/PORAAA-9)  
Parent asset pack: [PORAAA-4](/PORAAA/issues/PORAAA-4)

---

## Overview

This document describes the visual system, section behavior, and implementation constraints for the Agency Swarm launch landing page. It is designed to be built by Engineering without inventing messaging or layout.

The page is a single-scroll experience with seven sections:
1. Navigation
2. Hero
3. Proof strip
4. Problem / Solution
5. Outcomes
6. Credibility
7. Final CTA + Footer

All copy is drawn directly from the PORAAA-4 message spine and is evidence-safe. No claims exceed what is visible in the repo, docs, or commits today.

---

## Visual System

### Palette

Derived from the existing Agency Swarm visualization UI (`src/agency_swarm/ui/templates/html/`).

| Token | Hex | Usage |
|-------|-----|-------|
| Primary 600 | `#667eea` | Gradients, links, buttons |
| Primary 700 | `#5a67d8` | Link hover |
| Accent 600 | `#764ba2` | Gradients, headline texture |
| Emerald | `#10b981` | Positive signals, checks |
| Rose | `#f43f5e` | Problem card accent |
| Amber | `#f59e0b` | Problem card accent (secondary) |
| Surface | `#ffffff` | Page background |
| Surface Raised | `#f8fafc` | Alternating section background |
| Surface Dark | `#0f172a` | CTA section background |
| Text | `#0f172a` | Headings, body |
| Text Secondary | `#475569` | Subheadings, descriptions |
| Text Tertiary | `#64748b` | Micro copy, metadata |

### Typography

- **Font family**: `system-ui` stack. No external font files. Fast first paint.
- **Scale**: Fluid but anchored to rem units. Base is `1rem` (16px).
- **Hero headline**: `3.75rem` on desktop, gradient text fill using `background-clip: text`.
- **Section titles**: `1.875rem` desktop, tight line-height (`1.2`).
- **Body**: `1rem` / `1.5` line-height, max `55ch` width for readability.

### Spacing

- Vertical section padding: `6rem` mobile, `8rem` desktop.
- Container max-width: `75rem` (1200px) with responsive inline padding.
- Component gap: `1.5rem` base, scaling to `2rem` on desktop.

### Motion

- **Philosophy**: Motion supports hierarchy, not decoration.
- **Hero nodes**: CSS `float` keyframe animation (8–12s, infinite, ease-in-out). Pure CSS, no JS.
- **Buttons**: `transform: translateY(-1px)` + shadow lift on hover. `150ms` transition.
- **Scroll**: Native `scroll-behavior: smooth`. No scroll-jacking libraries.
- **Nav**: `backdrop-filter: blur(12px)` with transparent-to-solid transition on scroll.

---

## Section Breakdown

### 1. Navigation

**Behavior:**
- Fixed top, full width.
- Mobile: hamburger toggle with `aria-expanded` state.
- Desktop: inline links + CTA button.
- Scrolls with page; no hide/show on scroll to keep CTA always accessible.

**Responsive:**
- `sm` (640px): Show desktop nav, hide mobile toggle.
- Below `sm`: Show toggle, hide inline links.

**Engineering notes:**
- The mobile menu uses `[hidden]` attribute toggled by JS. CSS ensures `display: none` when hidden.
- Nav CTA is identical styling to hero primary button but smaller.

---

### 2. Hero

**Layout:**
- Centered text block over an ambient background illustration.
- Background: `hero-orbit` contains 3 floating nodes and 3 connecting edges. Pure CSS; no canvas, no animation library.

**Content:**
- Eyebrow: "Open-source multi-agent orchestration"
- Headline: "Stop running your swarm by hand."
- Subheadline: Full description from PORAAA-4.
- Primary CTA: "Book a workflow teardown"
- Secondary CTA: "View the repo on GitHub"
- Micro: Run anchor code tag.

**Responsive:**
- Headline: `2.25rem` → `3rem` → `3.75rem`
- CTAs stack vertically on mobile, row on `sm`+
- Background illustration scales with viewport; nodes positioned in `%` so they remain relative.

**Accessibility:**
- Background is `aria-hidden="true"` and `pointer-events: none`.
- `prefers-reduced-motion`: Add media query to disable `float` animation.

---

### 3. Proof Strip

**Layout:**
- Horizontal flex list, centered, wrapping.
- Each item: green check circle + text.

**Content (from PORAAA-4):**
1. Built on the OpenAI Agents SDK
2. Explicit communication flows between agents
3. Type-safe tools with Pydantic validation
4. Proof-of-progress commits tied to this launch

**Responsive:**
- `default`: 1–2 columns, wrap.
- `lg` (1024px): Single row with more generous gap.

---

### 4. Problem / Solution

**Layout:**
- Two-column grid (`grid-two`).
- Left: Problem card (rose/amber top border).
- Right: Solution card (emerald/primary top border).

**Content:**
- Problem: Three bullet points about fragile handoffs, hidden state, manual work.
- Solution: Three bullet points about explicit flows, typed tools, thread callbacks.

**Responsive:**
- Below `md` (768px): Stacks to single column.
- Cards maintain equal height when side-by-side.

**Engineering notes:**
- Cards use `::before` pseudo-element for top accent border.
- Bullet points use `::before` colored dots. No `list-style` needed.

---

### 5. Outcomes

**Layout:**
- Three-column grid.
- Each outcome: centered icon (SVG) + title + description.

**Content (from PORAAA-4):**
1. Less repeated manual work
2. Standardized across teams
3. Grounded in explicit contracts

**Responsive:**
- Below `md`: Single column.
- `md`+: Three equal columns.

**Icons:**
- Inline SVGs, `stroke="currentColor"`, no icon library dependency.
- Icons are decorative; `aria-hidden="true"`.

---

### 6. Credibility

**Layout:**
- Three-column grid.
- Each item: large background number (`01`, `02`, `03`) + title + body.

**Content (from PORAAA-4):**
1. Open-source framework
2. Run anchor (`20260420T210900Z`)
3. OpenAI Agents SDK foundation

**Responsive:**
- Below `md`: Single column.
- Numbers scale to `3rem` font size; should not overflow on narrow screens.

---

### 7. Final CTA + Footer

**CTA Layout:**
- Dark background (`#0f172a`).
- Centered headline, body, dual CTAs, micro-link.
- Subtle radial gradient glow at top (pure CSS).

**CTA Content:**
- Headline: "Bring one broken workflow."
- Body: "We will map it to an explicit swarm flow in 20 minutes..."
- Primary CTA: "Book a 20-minute teardown"
- Secondary CTA: "Run the starter template"
- Micro: Async issue link with run tag.

**Footer Layout:**
- Simple bar: copyright left, links right.
- Mobile: centered stack.

---

## Responsive Breakpoints

| Name | Width | Key Changes |
|------|-------|-------------|
| Default | < 640px | Single column, stacked CTAs, mobile nav |
| `sm` | >= 640px | Inline CTAs, larger type, 2-col grids |
| `md` | >= 768px | Problem/Solution side-by-side, outcomes 3-col |
| `lg` | >= 1024px | Full section padding, proof strip single row |
| `xl` | >= 1280px | Max container width reached |

---

## Performance & Constraints

1. **No external dependencies**: No JS frameworks, no icon libraries, no font CDNs.
2. **No images**: All visuals are CSS or inline SVG. Zero image requests.
3. **No analytics scripts**: Engineering should add tracking only after design review.
4. **Accessibility**:
   - All interactive elements have focus states (browser default is acceptable).
   - Color contrast meets WCAG AA for all text/background pairs.
   - `aria-label` and `aria-labelledby` used on sections and nav.
5. **Reduced motion**: Respect `prefers-reduced-motion` by disabling `float` animation.

---

## Files

| File | Purpose |
|------|---------|
| `index.html` | Semantic markup, inline SVG icons, minimal JS for nav + smooth scroll |
| `landing.css` | Complete visual system, responsive styles, CSS animations |
| `DESIGN.md` | This document — rationale, section notes, engineering constraints |

---

## Evidence Guardrails

All claims on this page are scoped to the current repo state at run `20260420T210900Z`.

- **Do not** add metrics ("10x faster", "99% uptime") that are not in the repo or docs.
- **Do not** add testimonials or logos unless they exist in the trust packet.
- **Do not** change the CTA to "Buy" or "Sign up" — the current CTAs (book teardown, view repo, run starter) match the evidence-safe position.

If the product evolves, update `DESIGN.md` and the copy in `index.html` together. Never let the visual system drift from the message spine.

---

## Handoff Checklist

- [ ] Engineering confirms all seven sections render correctly on desktop + mobile
- [ ] Engineering adds `prefers-reduced-motion` media query if not already present
- [ ] Engineering verifies nav scroll behavior (optional JS to add `.scrolled` class)
- [ ] Engineering connects CTA buttons to real URLs (Calendly, GitHub, Discord)
- [ ] QA verifies color contrast with automated tool (Lighthouse, axe)
- [ ] Designer reviews built page before merge to `main`

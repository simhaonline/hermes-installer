# Sovereign Institutional Design System & Brand Guidelines
**Aesthetic Standard:** Swiss Private Banking, High-End Editorial & Institutional Ledger  
**Version:** 1.0.0 (Nameless / White-Label Edition)  
**Target Applications:** High-End Fintech, Private Wealth, Commodities, B2B SaaS, Sovereign Treasuries, Enterprise Platforms  

---

## 1. Design Philosophy & Aesthetic Tenets

This design system is built to communicate **stability, institutional gravity, precision, and quiet luxury**. It is completely brand-agnostic and ready to be deployed across any platform.

### Core Visual Principles
1. **Zero Card-Soup & Zero Clutter:** Avoid floating pastel cards with heavy artificial drop-shadows. The layout relies on structured horizontal planes, clean sections, and high-confidence whitespace.
2. **Hairline Precision:** All structural divisions use razor-thin `1px` borders (`#E5E9F0`). Dividers feel like crisp architectural rules.
3. **Stately Editorial Typography:** Contrast high-dignity serif display headers (`Cormorant Garamond`) with ultra-legible, geometric neo-grotesque body copy (`Plus Jakarta Sans`) and financial-grade monospace digits (`IBM Plex Mono`).
4. **Authoritative Midnight Canvas:** High-contrast pairing of deep sovereign navy (`#0C1E36`, `#071324`) with pure crisp white (`#FFFFFF`) and warm editorial paper tones (`#FBFBFC`).
5. **Precision Jewel Accents:** A curated spectrum of jewel tones (Gold `#FBBA03`, Green `#88BD31`, Turquoise `#16A7B5`, Orange `#F18D58`, Blue `#156BA6`) used deliberately for metrics, indicators, and status signals.

---

## 2. Complete Master Color System

All values are specified in **HEX**, **RGB**, **HSL**, and **CMYK** (for print and physical media), with contrast scores and semantic assignments.

### 2.1 Sovereign Navy Core (Surfaces, Headers & Primary Actions)

| Token Name | Role / Function | HEX | RGB | HSL | CMYK | WCAG on Light | WCAG on Dark |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `--corp-navy-deep` | Deepest Background / Footer / Hero Dark | `#071324` | `7, 19, 36` | `215°, 67%, 8%` | `81, 47, 0, 86` | 17.5:1 (AAA) | Surface |
| `--corp-navy-primary` | Primary Brand / Action Buttons / Main Headers | `#0C1E36` | `12, 30, 54` | `214°, 64%, 13%` | `78, 44, 0, 79` | 15.2:1 (AAA) | Surface |
| `--corp-navy-surface` | Elevated Dark Cards / Tooltips / Dark Panels | `#142844` | `20, 40, 68` | `215°, 55%, 17%` | `71, 41, 0, 73` | 12.8:1 (AAA) | 1.3:1 |
| `--corp-navy-subtle` | Soft Navy Tint / Subtle Hover States | `rgba(12, 30, 54, 0.04)` | `12, 30, 54, 0.04` | — | — | Decorative | Decorative |
| `--corp-navy-border` | Subtle Navy Hairline on Light Surfaces | `rgba(12, 30, 54, 0.12)` | `12, 30, 54, 0.12` | — | — | Decorative | Decorative |
| `--corp-navy-slate` | Secondary Corporate Navy / Wordmark Ink | `#2E3761` | `46, 55, 97` | `229°, 36%, 28%` | `53, 43, 0, 62` | 9.8:1 (AAA) | 2.1:1 |
| `--corp-navy-muted` | Tertiary Cool Navy / Badge Ink | `#344069` | `52, 64, 105` | `226°, 34%, 31%` | `50, 39, 0, 59` | 8.2:1 (AAA) | 2.6:1 |

### 2.2 Noble Jewel & Geometric Accent Palette

Use these high-precision tones for micro-accents, data visualization, tags, charts, and telemetry:

| Accent Name | Token Name | HEX | RGB | HSL | CMYK | Semantic Role |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Heraldic Gold** | `--accent-gold` | `#FBBA03` | `251, 186, 3` | `44°, 98%, 50%` | `0, 26, 99, 2` | Premium tier, certified status, gold bullion, star rating |
| **Geometric Yellow** | `--accent-yellow` | `#E8E006` | `232, 224, 6` | `58°, 95%, 47%` | `0, 3, 97, 9` | Apex dynamic highlight, attention alert |
| **Geometric Green** | `--accent-green` | `#88BD31` | `136, 189, 49` | `83°, 59%, 47%` | `28, 0, 74, 26` | Sustainability, ESG metrics, verified security, growth |
| **Geometric Turquoise**| `--accent-cyan` | `#16A7B5` | `22, 167, 181` | `185°, 78%, 40%` | `88, 8, 0, 29` | Purity analysis, technical precision, calibration |
| **Geometric Orange** | `--accent-orange` | `#F18D58` | `241, 141, 88` | `21°, 85%, 65%` | `0, 41, 63, 5` | Energy, active operational process, heat / thermal state |
| **Geometric Blue** | `--accent-blue` | `#156BA6` | `21, 107, 166` | `204°, 78%, 37%` | `87, 36, 0, 35` | Custody, security, logistics, maritime / air transport |

### 2.3 Canvases & Neutral Surfaces

| Token Name | HEX | RGB | HSL | Semantic Application |
| :--- | :--- | :--- | :--- | :--- |
| `--corp-canvas` | `#FFFFFF` | `255, 255, 255` | `0°, 0%, 100%` | Primary base canvas, input backgrounds, modal surfaces |
| `--corp-canvas-warm` | `#FBFBFC` | `251, 251, 252` | `240°, 14%, 99%` | Warm alternating section canvas (prestige editorial feel) |
| `--corp-canvas-elevated`| `#F4F6F9` | `244, 246, 249` | `216°, 27%, 97%` | Hover fills, table alternate rows, secondary cards |

### 2.4 Hairlines & Border Dividers

| Token Name | HEX | RGB | HSL | Semantic Application |
| :--- | :--- | :--- | :--- | :--- |
| `--corp-border` | `#E5E9F0` | `229, 233, 240` | `218°, 24%, 92%` | Standard 1px structural hairlines, table borders, dividers |
| `--corp-border-subtle` | `#F0F3F7` | `240, 243, 247` | `214°, 30%, 95%` | Quiet interior grid dividers, nested list separators |
| `--corp-border-strong` | `#CBD5E1` | `203, 213, 225` | `213°, 27%, 84%` | Button outlines, input border defaults, focused containers |

### 2.5 Typography & Content Inks

| Token Name | HEX | RGB | Semantic Role | Contrast on White |
| :--- | :--- | :--- | :--- | :--- |
| `--corp-text-primary` | `#0F172A` | `15, 23, 42` | Pitch Charcoal for main headings and titles | 16.5:1 (AAA) |
| `--corp-text-secondary`| `#334155` | `51, 65, 85` | Slate for editorial body copy & paragraphs | 9.7:1 (AAA) |
| `--corp-text-muted` | `#64748B` | `100, 116, 139`| Muted metadata, timestamps, table labels | 4.8:1 (AA) |
| `--corp-text-on-dark` | `#F8FAFC` | `248, 250, 252`| High-contrast body text on navy backgrounds | 15.1:1 on `#0C1E36` |
| `--corp-text-inverse` | `#FFFFFF` | `255, 255, 255`| Pure white headings on dark surfaces | 15.2:1 on `#0C1E36` |

### 2.6 Operational & Market Status Signals

| Status Role | Token | HEX | RGB | Semantic Application |
| :--- | :--- | :--- | :--- | :--- |
| **Positive / Up** | `--status-up` | `#15803D` | `21, 128, 61` | Price gain, verified integrity, healthy operational status |
| **Warning / Down** | `--status-down` | `#B91C1C` | `185, 28, 28` | Price decline, system warning, threshold near capacity |
| **Critical Danger**| `--status-danger`| `#DC2626` | `220, 38, 38` | Tamper detection, security breach, transaction failure |
| **Neutral / Hold** | `--status-neutral`| `#475569` | `71, 85, 105` | Inactive, pending review, offline, escrow locked |

---

## 3. Typography Architecture

### 3.1 Font Families

```css
/* Display / Headings (Stately Heritage Serif) */
--font-display: 'Cormorant Garamond', Garamond, Georgia, serif;

/* Body / Interface (Ultra-Clean Modern Sans) */
--font-body: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

/* Numeric / Ledger / Code (Strict Financial Monospace) */
--font-mono: 'IBM Plex Mono', 'SF Mono', Consolas, monospace;
```

#### Google Fonts Embed Snippet
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500;600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

### 3.2 Typographic Hierarchy & Scale

| Level | Element / Selector | Typeface | Fluid Clamp Size | Line Height | Letter Spacing | Weight |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Hero Title** | `h1` | Cormorant Garamond | `clamp(2.6rem, 5.2vw, 4.2rem)` | `1.12` | `-0.01em` | `600` |
| **Section Header** | `h2` | Cormorant Garamond | `clamp(2.0rem, 3.6vw, 3.0rem)` | `1.18` | `-0.01em` | `600` |
| **Subsection Header**| `h3` | Cormorant Garamond | `clamp(1.4rem, 2.4vw, 2.0rem)` | `1.25` | `-0.005em` | `600` |
| **Minor Header** | `h4` | Cormorant Garamond | `clamp(1.15rem, 1.8vw, 1.4rem)`| `1.30` | `0` | `600` |
| **Eyebrow Label** | `.eyebrow` | Plus Jakarta Sans | `0.75rem (12px)` | `1.2` | `0.16em` | `600 (Uppercase)` |
| **Lead Paragraph** | `.lead` | Plus Jakarta Sans | `1.15rem (18.4px)` | `1.75` | `-0.005em` | `400` |
| **Standard Body** | `p`, `body` | Plus Jakarta Sans | `1.0rem (16px)` | `1.75` | `-0.005em` | `400` |
| **Small / Meta** | `small`, `.caption`| Plus Jakarta Sans | `0.85rem (13.6px)` | `1.5` | `0` | `400 / 500` |
| **Ledger / Numeric** | `.numeric`, `code` | IBM Plex Mono | `0.92rem (14.7px)` | `1.4` | `0` | `500 / 600` |

---

## 4. Spacing, Geometry & Layout Architecture

### 4.1 8-Point Spatial Scale
```css
--space-xs:  0.25rem;   /* 4px   - Inner badge padding, micro gaps */
--space-sm:  0.5rem;    /* 8px   - Icon margins, eyebrow offsets */
--space-md:  1.0rem;    /* 16px  - Form inputs, standard padding */
--space-lg:  1.5rem;    /* 24px  - Column gutters, card insets */
--space-xl:  2.0rem;    /* 32px  - Container margins, row spacing */
--space-2xl: 3.5rem;    /* 56px  - Sub-section vertical rhythms */
--space-3xl: 5.0rem;    /* 80px  - Major section gaps */
--space-4xl: 6.5rem;    /* 104px - Primary section top/bottom breathing room */
```

### 4.2 Corner Radii (Anti-Bubble Standard)
Do not use oversized rounded corners. Keep elements crisp and architectural:
* `--radius-sm: 4px` (Buttons, form fields, badges, code blocks)
* `--radius-md: 6px` (Modals, dialogs, elevated containers)
* `--radius-full: 9999px` (Pill status dots only)

### 4.3 Layout Grid & Container Dimensions
* Standard Container: `1240px` (`--container-max`)
* Wide Panorama Container: `1360px` (`--container-wide`)
* Narrow Reading Container: `860px` (`--container-narrow`)
* Navigation Bar Height: `74px` (`--nav-height`)
* Utility / Ticker Bar Height: `36px` (`--utility-height`)

---

## 5. UI Primitives & Layout Patterns

### 5.1 Button Hierarchy

```css
/* Universal Base Primitive */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.85rem 1.8rem;
  font-family: var(--font-body);
  font-size: 0.88rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  border-radius: var(--radius-sm); /* 4px */
  transition: all 150ms cubic-bezier(0.16, 1, 0.3, 1);
  white-space: nowrap;
  line-height: 1;
  cursor: pointer;
}

/* Primary Action Button (Solid Sovereign Navy) */
.btn-primary {
  background: var(--corp-navy-primary); /* #0C1E36 */
  color: #FFFFFF;
  border: 1px solid var(--corp-navy-deep);
}
.btn-primary:hover {
  background: var(--corp-navy-deep); /* #071324 */
  color: #FFFFFF;
}

/* Secondary Button (Crisp White on Hairline Border) */
.btn-secondary {
  background: #FFFFFF;
  color: var(--corp-navy-primary);
  border: 1px solid var(--corp-border-strong); /* #CBD5E1 */
}
.btn-secondary:hover {
  background: var(--corp-canvas-elevated); /* #F4F6F9 */
  border-color: var(--corp-navy-primary);
}

/* Outline Ghost Button */
.btn-outline {
  background: transparent;
  color: var(--corp-text-secondary);
  border: 1px solid var(--corp-border-strong);
}
.btn-outline:hover {
  color: var(--corp-navy-primary);
  border-color: var(--corp-navy-primary);
  background: var(--corp-canvas-warm);
}

/* Compact Button */
.btn-sm {
  padding: 0.5rem 1.1rem;
  font-size: 0.82rem;
}
```

### 5.2 Two-Column Editorial Row (Replaces Cluttered Cards)

Instead of nesting information inside floating shadow cards, lay content out in structured horizontal planes:

```css
.editorial-row {
  display: grid;
  grid-template-columns: 1fr 1.6fr;
  gap: var(--space-3xl); /* 80px */
  padding: var(--space-2xl) 0; /* 56px */
  border-top: 1px solid var(--corp-border); /* 1px #E5E9F0 */
  align-items: flex-start;
}

@media (max-width: 860px) {
  .editorial-row {
    grid-template-columns: 1fr;
    gap: var(--space-md);
    padding: var(--space-xl) 0;
  }
}
```

### 5.3 Institutional Specification Table

```css
.spec-table {
  width: 100%;
  border-collapse: collapse;
}

.spec-table tr {
  border-bottom: 1px solid var(--corp-border); /* 1px #E5E9F0 */
}

.spec-table td {
  padding: 1.1rem 0;
  font-size: 0.92rem;
  color: var(--corp-text-secondary);
}

.spec-table td:first-child {
  color: var(--corp-text-muted); /* #64748B */
  font-weight: 500;
  width: 40%;
}

.spec-table td:last-child {
  font-weight: 600;
  color: var(--corp-text-primary); /* #0F172A */
  text-align: right;
  font-family: var(--font-mono); /* For numbers/serials */
}
```

---

## 6. Code Exports for Other Projects

### 6.1 Complete CSS Variables File (`design-tokens.css`)

```css
:root {
  /* Surfaces & Canvases */
  --corp-canvas: #FFFFFF;
  --corp-canvas-warm: #FBFBFC;
  --corp-canvas-elevated: #F4F6F9;

  /* Sovereign Navy Palette */
  --corp-navy-deep: #071324;
  --corp-navy-primary: #0C1E36;
  --corp-navy-surface: #142844;
  --corp-navy-subtle: rgba(12, 30, 54, 0.04);
  --corp-navy-border: rgba(12, 30, 54, 0.12);
  --corp-navy-slate: #2E3761;
  --corp-navy-muted: #344069;

  /* Jewel Accents */
  --accent-gold: #FBBA03;
  --accent-yellow: #E8E006;
  --accent-green: #88BD31;
  --accent-cyan: #16A7B5;
  --accent-orange: #F18D58;
  --accent-blue: #156BA6;

  /* Hairlines & Borders */
  --corp-border: #E5E9F0;
  --corp-border-subtle: #F0F3F7;
  --corp-border-strong: #CBD5E1;

  /* Typography Inks */
  --corp-text-primary: #0F172A;
  --corp-text-secondary: #334155;
  --corp-text-muted: #64748B;
  --corp-text-on-dark: #F8FAFC;
  --corp-text-inverse: #FFFFFF;

  /* Status Signals */
  --status-up: #15803D;
  --status-down: #B91C1C;
  --status-danger: #DC2626;
  --status-neutral: #475569;

  /* Fonts */
  --font-display: 'Cormorant Garamond', Garamond, Georgia, serif;
  --font-body: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono: 'IBM Plex Mono', 'SF Mono', Consolas, monospace;

  /* Spacing */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1.0rem;
  --space-lg: 1.5rem;
  --space-xl: 2.0rem;
  --space-2xl: 3.5rem;
  --space-3xl: 5.0rem;
  --space-4xl: 6.5rem;

  /* Geometry & Radii */
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-full: 9999px;

  /* Dimensions */
  --container-max: 1240px;
  --container-wide: 1360px;
  --container-narrow: 860px;
  --nav-height: 74px;
  --utility-height: 36px;
}
```

### 6.2 Tailwind CSS Configuration (`tailwind.config.js`)

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  theme: {
    extend: {
      colors: {
        institutional: {
          navy: {
            deep: '#071324',
            DEFAULT: '#0C1E36',
            surface: '#142844',
            slate: '#2E3761',
            muted: '#344069',
          },
          gold: '#FBBA03',
          yellow: '#E8E006',
          green: '#88BD31',
          cyan: '#16A7B5',
          orange: '#F18D58',
          blue: '#156BA6',
          canvas: {
            DEFAULT: '#FFFFFF',
            warm: '#FBFBFC',
            elevated: '#F4F6F9',
          },
          border: {
            DEFAULT: '#E5E9F0',
            subtle: '#F0F3F7',
            strong: '#CBD5E1',
          },
          text: {
            primary: '#0F172A',
            secondary: '#334155',
            muted: '#64748B',
            onDark: '#F8FAFC',
          },
          status: {
            up: '#15803D',
            down: '#B91C1C',
            danger: '#DC2626',
            neutral: '#475569',
          }
        }
      },
      fontFamily: {
        display: ['"Cormorant Garamond"', 'Garamond', 'Georgia', 'serif'],
        sans: ['"Plus Jakarta Sans"', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'sans-serif'],
        mono: ['"IBM Plex Mono"', 'Consolas', 'monospace'],
      },
      borderRadius: {
        'inst-sm': '4px',
        'inst-md': '6px',
      },
      maxWidth: {
        'inst': '1240px',
        'inst-wide': '1360px',
        'inst-narrow': '860px',
      }
    }
  }
};
```

---

## 7. Universal AI Model System Prompt (Drop-in for Any Project)

Whenever you prompt an AI coding assistant (ChatGPT, Claude, Gemini, Antigravity, Cursor) to build an application or page in this aesthetic, provide this exact design directive:

```markdown
Design this application according to the "Sovereign Institutional Editorial" design system (inspired by Swiss private banking and high-end financial institutions):

1. Color Palette:
   - Primary Surface / Canvases: Pure Canvas White (#FFFFFF), Warm Editorial Canvas (#FBFBFC), Elevated Gray (#F4F6F9).
   - Core Navy: Deep Midnight (#071324), Sovereign Navy Primary (#0C1E36), Elevated Dark Surface (#142844).
   - Hairline Borders: Razor-thin 1px dividers (#E5E9F0), Strong Border (#CBD5E1).
   - Inks: Pitch Charcoal (#0F172A) for headers, Slate Body (#334155), Muted Gray (#64748B) for labels.
   - Jewel Accents: Gold (#FBBA03), Green (#88BD31), Turquoise (#16A7B5), Orange (#F18D58), Blue (#156BA6).
   - Status Signals: Up (#15803D), Down (#B91C1C), Danger (#DC2626).

2. Typography:
   - Headings (H1, H2, H3): 'Cormorant Garamond', Georgia, serif (Font weight 600, tight letter-spacing -0.01em).
   - Body & UI: 'Plus Jakarta Sans', sans-serif (Font weight 400 for text, 600 for buttons).
   - Numbers, Ledger, Codes, Metrics: 'IBM Plex Mono', monospace (Font weight 500/600).
   - Eyebrows: 0.75rem (12px), uppercase, letter-spacing 0.16em, bold.

3. Spatial Layout & Rules:
   - Strictly ZERO card-clutter and ZERO heavy drop-shadows. No bubbly rounded cards.
   - Use structured two-column editorial rows (grid-template-columns: 1fr 1.6fr) divided by clean 1px hairline borders (border-top: 1px solid #E5E9F0).
   - Corner Radius: Crisp and architectural (border-radius: 4px for buttons and inputs).
   - Primary Buttons: Solid Navy (#0C1E36) with crisp white text.
   - Secondary Buttons: Pure White with #CBD5E1 hairline border.
```

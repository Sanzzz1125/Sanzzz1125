# 🚀 Alassa Technology Solutions (Alassatech) — Enterprise Agentic AI Platform
**Comprehensive Technical Architecture, Design System & Codebase Documentation**

> **Welcome to the Alassatech Codebase!**  
> This document provides an **exhaustive, inch-by-inch, file-by-file architectural blueprint** of the entire Alassatech web application. Whether you are a new developer onboarding to the project, an architect reviewing the system design, or a designer exploring the UI/UX tokens, this guide will orient you completely from A to Z. By reading this document, you will understand exactly **how the platform is built, where every component lives, how styling and design tokens work, how environment variables are configured, and how client-side behaviors operate.**

---

## 📋 Table of Contents
1. [Executive Summary & Platform Vision](#1-executive-summary--platform-vision)
2. [Technology Stack & Architectural Principles](#2-technology-stack--architectural-principles)
3. [Environment Variables & Configuration Guide](#3-environment-variables--configuration-guide)
4. [Design System & Theme Architecture (Inch-by-Inch)](#4-design-system--theme-architecture-inch-by-inch)
   - [Color Palette & Token Definitions](#color-palette--token-definitions)
   - [Typography & Font Stack](#typography--font-stack)
   - [Spatial, Spacing & Layout Tokens](#spatial-spacing--layout-tokens)
   - [Border Radii & Elevation/Shadow System](#border-radii--elevationshadow-system)
5. [Dynamic Interactions & Micro-Animations](#5-dynamic-interactions--micro-animations)
6. [Exhaustive File-by-File & Directory Map](#6-exhaustive-file-by-file--directory-map)
   - [Root Configuration Files](#root-configuration-files)
   - [Public Assets & Media (`public/`)](#public-assets--media-public)
   - [Next.js App Router Pages (`src/app/`)](#nextjs-app-router-pages-srcapp)
   - [Shared Stylesheets (`src/app/assets/css/`)](#shared-stylesheets-srcappassetscss)
   - [Reusable UI Components (`src/components/`)](#reusable-ui-components-srccomponents)
7. [Responsive Breakpoint Architecture](#7-responsive-breakpoint-architecture)
8. [Key Technical Workflows & Integrations](#8-key-technical-workflows--integrations)
   - [Web3Forms Serverless Contact Pipeline](#web3forms-serverless-contact-pipeline)
   - [IntersectionObserver Scroll Reveal Engine](#intersectionobserver-scroll-reveal-engine)
   - [Frosted Glassmorphism Navbar State](#frosted-glassmorphism-navbar-state)
9. [Local Development, Build & Deployment Guide](#9-local-development-build--deployment-guide)
   - [Step-by-Step Onboarding for New Employees](#step-by-step-onboarding-for-new-employees)
   - [Production Build & Verification](#production-build--verification)
   - [Deployment Instructions (Vercel & Docker/VPS)](#deployment-instructions-vercel--dockervps)

---

## 1. Executive Summary & Platform Vision

**Alassatech** is an enterprise-grade web application showcasing cutting-edge **Agentic Video-as-a-Service (VaaS)** and AI automation platforms. Designed specifically for **Higher Education** (MBA admissions, mock interview training, viva evaluations) and **Enterprise Workflows** (document intelligence, automated drafting, autonomous task agents), the website is built to impress at first glance with vibrant aesthetics, dark mode accents, glassmorphism, and fluid micro-animations.

The codebase prioritizes **zero CSS-framework bloat**, relying entirely on modern **Vanilla CSS with strict Design Tokens (`:root` CSS variables)** combined with the power of the **Next.js 15 App Router** and **TypeScript**.

---

## 2. Technology Stack & Architectural Principles

| Layer / Technology | Choice & Implementation | Purpose & Benefit |
| :--- | :--- | :--- |
| **Core Framework** | **Next.js 15.1.0** (App Router) | Provides server-side rendering (SSR), static site generation (SSG), file-system routing, and optimized layout persistence across navigation. |
| **Language** | **TypeScript 5.0+** (`.tsx` / `.ts`) | Ensures strict type safety, zero runtime interface mismatches, and robust IDE auto-completion across all React components. |
| **UI Library** | **React 19.0.0** | Powers modern functional components and declarative user interfaces with server and client boundaries (`'use client'`). |
| **Styling Architecture** | **Vanilla CSS & Design Tokens** | **No TailwindCSS or Bootstrap bloat.** Uses custom CSS variables defined in `:root`, global shared sheets (`shared.css`, `index_core.css`), and modular scoped page styles for maximum rendering speed and pixel-perfect design control. |
| **Typography Engine** | **Google Inter** via `next/font/google` | Zero-layout-shift font optimization, self-hosted automatically by Next.js at build time, with fallback system fonts and Georgia serif decorative accents. |
| **Form Backend** | **Web3Forms Serverless API** | Pure client-side `fetch()` API integration (`https://api.web3forms.com/submit`) allowing seamless email contact submissions without managing backend servers or databases. |
| **Media Player** | **Native HTML5 Video API** | High-performance containerized MP4 video streaming for product demonstrations (`Conversational Bot.mp4`, etc.) with zero third-party player overhead. |
| **DOM Animations** | **Native IntersectionObserver API** | Lightweight client-side scroll reveal animation trigger without heavy external animation libraries. |

---

## 3. Environment Variables & Configuration Guide

To maintain security, flexibility, and seamless environment migration across development, staging, and production, Alassatech uses environment variables for sensitive access keys, email addresses, WhatsApp numbers, and site URLs.

### Required Environment Variables

When onboarding as a new employee or setting up a local development environment, create a `.env.local` file in the root of the project (`alassa-nextjs/`) with the following structure:

```env
# ─── Form Submission Backend ──────────────────────────────────────
# Web3Forms API Access Key (Required for /contact form submissions)
NEXT_PUBLIC_WEB3FORMS_ACCESS_KEY="a501397c-5a04-4c76-9a37-e25f3900f7df"

# ─── Corporate Contact Information ────────────────────────────────
# Primary support and inquiry email displayed across footer, legal pages, and error fallbacks
NEXT_PUBLIC_CONTACT_EMAIL="techadmin@alassatech.in"

# WhatsApp Business number (Include country code without '+' symbol, e.g., 919176664239)
NEXT_PUBLIC_WHATSAPP_NUMBER="919176664239"

# ─── Application Routing ──────────────────────────────────────────
# Base domain URL for canonical links and API routing
NEXT_PUBLIC_SITE_URL="http://localhost:3000"
```

### How Environment Variables Are Used Across the Codebase
* **`src/app/contact/page.tsx`**: Reads `process.env.NEXT_PUBLIC_WEB3FORMS_ACCESS_KEY` to authenticate contact form submissions. Reads `process.env.NEXT_PUBLIC_CONTACT_EMAIL` for direct support email links and submission error fallbacks. Reads `process.env.NEXT_PUBLIC_WHATSAPP_NUMBER` for the floating chat button.
* **`src/components/Footer.tsx`**: Uses `process.env.NEXT_PUBLIC_CONTACT_EMAIL` for the primary contact email link and `process.env.NEXT_PUBLIC_WHATSAPP_NUMBER` for the WhatsApp quick action button.
* **`src/app/page.tsx`, `src/app/products/page.tsx`, `src/app/use-cases/page.tsx`**: All floating WhatsApp chat widgets dynamically interpolate `process.env.NEXT_PUBLIC_WHATSAPP_NUMBER`.
* **`src/app/terms/page.tsx` & `src/app/privacy/page.tsx`**: Legal inquiry and data retention email links dynamically read from `process.env.NEXT_PUBLIC_CONTACT_EMAIL`.

> **Note on Fallbacks**: All references in code are structured defensively with clean fallback defaults (e.g., `process.env.NEXT_PUBLIC_CONTACT_EMAIL || "techadmin@alassatech.in"`), ensuring zero runtime crashes even if an environment file is missing during local builds.

---

## 4. Design System & Theme Architecture (Inch-by-Inch)

The aesthetic excellence of Alassatech is controlled by a centralized set of **Design Tokens** defined in `:root`. Every component, button, card, and background strictly references these variables.

### Color Palette & Token Definitions

```
+----------------------------------------------------------------------------------------------------+
| ALASSATECH COLOR PALETTE SPECTRUM                                                                  |
+----------------------------------------------------------------------------------------------------+
| --navy (#0f172a)     ██████████  Deep Dark Slate: Used for dark theme sections, hero cards, footer |
| --blue-800 (#1e40af) ████████    Rich Navy Blue: Gradients and active button states                |
| --blue-700 (#1d4ed8) ████████    Deep Royal Blue: Gradient highlights and header accents           |
| --blue-600 (#0b4897) ██████      Primary Brand Blue: CTA buttons, interactive links, badge dots    |
| --blue-500 (#3b82f6) ████        Vibrant Electric Blue: Audio waveforms, hover accents, borders    |
| --blue-200 (#bfdbfe) ██          Soft Blue Glow: Subtle card hover borders and dark mode text      |
| --blue-100 (#dbeafe) █           Ice Blue: Step icon borders, decorative quotes                    |
| --blue-50 (#eff6ff)  ░           Ultra-Light Blue Tint: Button hover fills, badge backgrounds      |
+----------------------------------------------------------------------------------------------------+
| --teal (#0d9488)     ██████      Deep Teal: Accent radial gradients in hero orbs and contact form  |
| --teal-100 (#ccfbf1) ██          Light Teal Tint: Secondary badge highlights                       |
| --teal-50 (#f0fdfa)  ░           Soft Teal Mist: Background wash effects                           |
+----------------------------------------------------------------------------------------------------+
| --slate-700 (#334155)████████    Dark Charcoal: Primary outline button text, main headings         |
| --slate-600 (#475569)██████      Slate Gray: Marquee items, subheadings, body paragraphs           |
| --slate-500 (#64748b)████        Muted Gray: Form subheadings, secondary descriptions              |
| --slate-400 (#94a3b8)██          Light Slate: Muted captions, inactive icons                       |
| --slate-300 (#cbd5e1)█           Border Gray: Hero grid pattern dots, marquee separators           |
| --slate-200 (#e2e8f0)░           Card Border: Default container outlines, divider lines            |
| --slate-100 (#f1f5f9)            Off-White Gray: Form input backgrounds, FAQ hover states          |
| --white (#ffffff)                Pure White: Card containers, primary button text, page backgrounds|
+----------------------------------------------------------------------------------------------------+
| Functional Tokens:                                                                                 |
| --bg (#ffffff)       Primary section background (Pure White)                                       |
| --bg-alt (#f8faff)   Alternate section background (Soft Blue-White Tint for visual rhythm)         |
| --text-head (#0f172a)Primary Heading Typography Color (Deep Slate Navy)                            |
| --text-body (#475569)Primary Body Copy Color (Readable Slate Gray)                                 |
| --text-muted(#94a3b8)Secondary/Caption Typography Color (Muted Slate)                              |
| --border (#e2e8f0)   Universal Structural Border Color (Soft Slate 200)                            |
+----------------------------------------------------------------------------------------------------+
```

### Typography & Font Stack
* **Primary Font (`--font`)**: `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`.
  * Loaded via `next/font/google` in `src/app/layout.tsx` with `subsets: ['latin']` and `display: 'swap'`.
  * Global font smoothing is enabled: `-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;`.
* **Decorative Font**: `Georgia, serif` is used exclusively for the giant background quotation marks (`\201C`) inside customer testimonial cards (`.testi-card::before`).
* **Line Heights & Letter Spacing**:
  * Headings (`.hero-headline`, `.s-title`): `line-height: 1.08` to `1.15`, with tighter spacing (`letter-spacing: -0.03em` to `-0.025em`) for a bold, authoritative executive feel.
  * Body Copy (`.hero-sub`, `.step-desc`): `line-height: 1.6` to `1.75` for effortless reading comprehension.
  * Uppercase Labels (`.s-label`, `.ac-title`): `letter-spacing: 0.07em` to `0.1em`, `font-size: 0.7rem`, `font-weight: 700` for crisp metadata hierarchy.

### Spatial, Spacing & Layout Tokens
* **Max Container Width (`--max-w`)**: `1360px`. Center-aligned via `.container { margin: 0 auto; padding: 0 var(--px); }`.
* **Horizontal Gutters (`--px`)**: `1.5rem` (24px) on desktop, scaling down to `1.125rem` (18px) on mobile.
* **Vertical Section Spacing (`--section-py`)**: `5rem` (80px) on desktop, dynamically scaling down to `3.5rem` (56px) on mobile (`max-width: 767px`).

### Border Radii & Elevation/Shadow System
The UI uses a **5-tier border radius hierarchy** to create harmonious rounded geometry:
* `--r-sm: 6px` — Used for small internal tags, data cells (`.ac-cell`), and split badges.
* `--r: 10px` — The core standard radius for buttons (`.btn`), form input controls (`.form-control`), step icons, and navbar links.
* `--r-lg: 16px` — Used for medium structural containers: step cards (`.step`), value proposition cards (`.val-card`), use-case cards (`.uc-card`), and metric bars (`.fs-metrics`).
* `--r-xl: 24px` — Used for primary hero elements: dark Agent Cards (`.agent-card`), video presentation wrappers (`.video-wrap`), testimonial cards (`.testi-card`), CTA banners (`.cta-band`), and split contact form boxes.
* `--r-full: 9999px` — Perfectly circular pill badges (`.hero-badge`, `.pill`, `.ac-status`), status dots, and WhatsApp floating action buttons.

**Elevation & Box Shadows**:
* `--shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.07), 0 1px 2px rgba(0, 0, 0, 0.04)` — Subtle depth for floating pill badges.
* `--shadow: 0 4px 14px rgba(0, 0, 0, 0.08)` — Standard resting elevation for interactive cards.
* `--shadow-lg: 0 10px 32px rgba(0, 0, 0, 0.1)` — Expanded elevation triggered on hover (`.val-card:hover`, `.step:hover`).
* `--shadow-blue: 0 4px 18px rgba(37, 99, 235, 0.3)` — High-impact glowing blue shadow applied to primary CTA buttons (`.btn-primary`). When hovered, scales up to `0 6px 22px rgba(37, 99, 235, 0.38)`.

---

## 5. Dynamic Interactions & Micro-Animations

The codebase uses CSS keyframes and DOM observer hooks to create an interface that feels alive and interactive without slowing down rendering performance.

```
+----------------------------------------------------------------------------------------------------+
| SUMMARY OF LIVE MICRO-ANIMATIONS IN ALASSATECH                                                     |
+----------------------------------------------------------------------------------------------------+
| Animation Name    | Trigger / Target            | CSS Keyframes / Behavior                         |
+-------------------+-----------------------------+--------------------------------------------------+
| Scroll Reveal     | .reveal (via Observer)      | Translates Y from 28px to 0px, opacity 0 to 1    |
| Staggered Reveal  | .stagger > .reveal          | Sequential delays: 0.00s -> 0.12s -> 0.24s -> 0.36s|
| Orb Floating      | .hero-orb-1, .hero-orb-2    | 14s & 10s smooth diagonal translation (35px, -28px)|
| Live Waveform     | .wv (14 audio bars)         | 1.4s infinite vertical scaling (scaleY 0.4 to 1.0)|
| Button Shimmer    | .btn-primary::after         | 3s angled light reflection sweep from -100% to 220%|
| Infinite Marquee  | .marquee-track              | 24s linear X translation (0 to -50%), hover pause|
| Pulsing Dots      | .ac-status-dot, .badge-dot  | 1.5s / 2s opacity pulsing (opacity 0.3 to 1.0)   |
| WhatsApp Radar    | .wa-float::before           | 2.5s radar ring scale (0.9 to 1.3) with fade out |
| FAQ Accordion     | details[open] .faq-chevron  | 0.3s 180-degree smooth icon rotation on expand   |
+-------------------+-----------------------------+--------------------------------------------------+
```

### Detailed Breakdown of Key Micro-Animations:
1. **Real-Time Audio Waveform (`.waveform` & `.wv`)**:
   In the Hero section's dark "Agent Card", 14 vertical blue bars (`.wv`) simulate a live conversational AI voice processing audio. Each bar has a custom CSS height (ranging from 30% to 100%) and a unique animation delay (`0.00s`, `0.10s`, `0.55s`, etc.) running an infinite `wave` keyframe (`transform: scaleY(1); opacity: 1;`).
2. **Infinite Industry Marquee Ticker (`.marquee-track`)**:
   Displays a continuous horizontal scroll of client industries (Fintech, Healthcare, Higher Ed, etc.). Built using flexbox cloning and a `24s linear infinite` animation moving from `0` to `-50%`. To ensure usability, CSS includes `.marquee-track:hover { animation-play-state: paused; }`, allowing users to freeze the ticker to read an industry name.
3. **Button Light Sweep Shimmer (`@keyframes btn-shimmer`)**:
   Primary buttons feature an invisible pseudo-element (`::after`) with a `linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.22), transparent)`. Every 3 seconds, this light bar sweeps rapidly across the button from `left: -100%` to `left: 220%`, creating an ultra-premium metallic sheen.
4. **Frosted Glass Navbar Transition**:
   At the absolute top of the page (`scrollY <= 8`), the navbar is 100% transparent (`opacity: 0` background and border) so it blends seamlessly into the hero pattern. The moment the user scrolls down, `ClientScripts.tsx` adds the class `.is-scrolled` to `#nav`. CSS transitions smooth over `0.35s ease`:
   * Background becomes `rgba(255, 255, 255, 0.72)`.
   * Backdrop filter applies `blur(22px) saturate(180%)`, turning the header into a frosted glass pill where scrolling colors blur underneath without obscuring text.
   * A delicate border (`1px solid rgba(226, 232, 240, 0.8)`) and subtle drop shadow appear.

---

## 6. Exhaustive File-by-File & Directory Map

```
alassa-nextjs/
├── AGENTS.md                                # Custom behavioral instructions & rules for AI agents
├── CLAUDE.md                                # Project rules and codebase guidelines for Anthropic Claude
├── README.md                                # THIS FILE: Exhaustive architectural documentation
├── eslint.config.mjs                         # ESLint 9 flat configuration (Next.js core web vitals + TS rules)
├── next-env.d.ts                             # Next.js TypeScript environment declarations (auto-generated)
├── next.config.ts                            # Next.js compiler & routing configuration script
├── package.json                              # NPM dependencies, project metadata, and scripts (dev, build, start)
├── package-lock.json                         # Lockfile ensuring deterministic dependency installation
├── tsconfig.json                             # TypeScript compiler options (strict mode, path aliases @/* -> ./src/*)
├── tsconfig.tsbuildinfo                      # TypeScript incremental compilation cache
├── public/                                   # Static media root served at domain root (http://localhost:3000/*)
│   └── assets/
│       ├── Conversational Bot.mp4            # High-definition product demo video (Conversational AI agent)
│       ├── Document Assistant.mp4            # HD product video demonstrating AI RAG document comprehension
│       ├── Draft Response Feature.mp4        # HD product video showing automated enterprise email drafting
│       ├── Tasks.mp4                         # HD product video demonstrating autonomous workflow execution
│       └── images/
│           └── Alassatech_logo.png           # Official high-resolution brand logo (used in Navbar & Footer)
└── src/                                      # Primary application source code
    ├── app/                                  # Next.js App Router root directory
    │   ├── favicon.ico                       # Site browser tab icon
    │   ├── layout.tsx                        # Global Root Layout wrapper (Fonts, SEO metadata, Navbar/Footer)
    │   ├── page.tsx                          # Root Landing Page (/) - Core marketing homepage
    │   ├── contact/
    │   │   └── page.tsx                      # Interactive Contact Page (/contact) - Centered layout & Web3Forms API
    │   ├── products/
    │   │   └── page.tsx                      # Products Suite Page (/products) - Detailed AI agent suites & videos
    │   ├── use-cases/
    │   │   └── page.tsx                      # Industry Use-Cases Page (/use-cases) - Higher Ed & Enterprise solutions
    │   ├── product-video/
    │   │   └── page.tsx                      # Standalone Video Player Page (/product-video)
    │   ├── privacy/
    │   │   └── page.tsx                      # Legal Privacy Policy Page (/privacy)
    │   ├── terms/
    │   │   └── page.tsx                      # Legal Terms of Service Page (/terms)
    │   └── assets/
    │       └── css/
    │           ├── shared.css                # Global shared styles (Dropdown menus, navbar bridges, footer layouts)
    │           └── index_core.css            # Core design tokens (:root) and base resets imported in layout.tsx
    └── components/                           # Reusable modular React UI components
        ├── Navbar.tsx                        # Global Header Navbar with nested dropdowns & mobile drawer
        ├── Footer.tsx                        # Global 4-Column Footer with brand info, links, and WhatsApp CTA
        └── ClientScripts.tsx                 # Client-side DOM event controller (Scroll observer & shadow state)
```

### Inch-by-Inch File Descriptions

#### Root Configuration Files
* **`package.json`**: Defines scripts (`npm run dev` starts Next.js development server on port 3000, `npm run build` triggers optimized production bundle, `npm run start` serves production build). Core dependencies include `next@15.1.0`, `react@19.0.0`, `react-dom@19.0.0`. Dev dependencies include `typescript@5`, `@types/node`, `@types/react`, and `eslint`.
* **`tsconfig.json`**: Configures TypeScript compiler in strict mode. Employs path aliases where `@/*` maps directly to `./src/*`, allowing clean imports like `import Navbar from "@/components/Navbar";` without relative path clutter.
* **`next.config.ts`**: Standard Next.js configuration exported as a TypeScript module. Allows customized bundler rules, image domains, and headers.
* **`eslint.config.mjs`**: Modern flat configuration file for ESLint, applying `eslint-config-next` rules to enforce web vitals and React best practices during builds.

#### Public Assets & Media (`public/`)
* **`public/assets/images/Alassatech_logo.png`**: The single, authoritative brand logo for Alassa Technology Solutions. Rendered in the navbar (`height: 40px`) and footer (`height: 44px`) with `object-fit: contain`.
* **`public/assets/*.mp4`**: Four high-definition MP4 video demonstrations streamed directly from the domain root. Placed inside containerized `<video>` HTML5 elements with `autoplay`, `loop`, `muted`, and `playsinline` attributes for instant visual engagement without user interaction.

#### Next.js App Router Pages (`src/app/`)
* **`src/app/layout.tsx` (Root Layout - Server Component)**:
  * Employs `<html lang="en">` and injects the Google Inter font variable (`inter.className`).
  * Imports global CSS files in strict dependency order: `shared.css` followed by `index_core.css`.
  * Exports global SEO `<Metadata>` containing site title (`Alassa - Advanced Agentic Coding & Enterprise Solutions`), compelling meta descriptions, and viewport settings.
  * Structure: Wraps all child routes inside `<Navbar />`, `<main>{children}</main>`, `<Footer />`, and injects `<ClientScripts />` at the bottom to hydrate DOM interactivity across all route transitions.
* **`src/app/page.tsx` (Landing Page `/` - Server Component)**:
  * The showcase landing page. Contains modular section blocks styled with scoped CSS:
    * **Hero (`.hero`)**: Features a 2-column layout (`55% 1fr`). Left column houses the animated product badge (`.hero-badge`), bold headline (`.hero-headline` with gradient highlights `.hl`), subtitle, dual CTA buttons (`Request a Demo` and outline `Explore Products`), and a 3-metric statistics row (`.hero-stats` showing `10x Faster`, `24/7 Availability`, `99.9% Accuracy`). Right column hosts the interactive dark **Agent Card (`.agent-card`)** with live waveform bars and real-time meeting status simulation.
    * **Industry Marquee (`.marquee-section`)**: Seamless scrolling rail of vertical industries with SVG icon accents.
    * **How It Works (`.steps`)**: 4 horizontally interconnected cards (`.step`) with numerical badges (`01` to `04`), custom icons, and hover border highlights.
    * **Feature Band (`.fs-band`)**: High-contrast navy gradient banner featuring prominent stats (`500k+ Documents Analyzed`, `85% Cost Reduction`, `<1.5s Response Time`).
    * **Value Propositions (`.values`)**: 3-column grid of cards highlighting core differentiators (Enterprise Security, Seamless Integration, Custom AI Training).
    * **Use Cases (`.usecases`)**: 3-column grid showcasing tailored AI deployments for Higher Education, Financial Services, and Customer Support.
    * **Testimonials (`.testimonials-grid`)**: 2-column grid of social proof cards featuring 5-star ratings, author avatars, and Georgia serif background quote marks.
    * **FAQ (`.faq-list`)**: Built using semantic HTML5 `<details>` and `<summary>` tags (`.faq-item`, `.faq-q`). Includes animated chevron SVG rotation and CSS slide-down animations (`@keyframes faq-in`).
    * **CTA Banner (`.cta-band`)**: Dark rounded container with radial gradient background orbs urging visitors to book a demo.
* **`src/app/contact/page.tsx` (Contact Page `/contact` - Server/Client Hybrid Component)**:
  * Features a clean, **Centered Form Layout** designed for optimal conversion and user focus.
  * Hosts an elevated white form container (`.split-form-wrap`) centered on a light background. Features form groups for Name, Work Email, Phone Number (with `+91...` placeholder), Institution/Organization, Select Interest (MBA Admission Agent, Mock Interviews, Viva Evaluation, Custom VaaS), and an optional Message textarea.
  * **Interactive Submission Engine**: Houses an async client-side JavaScript submit handler (`submitContactForm`) wired directly to **Web3Forms API**.
* **`src/app/products/page.tsx` (`/products`)**:
  * Deep-dive product suite page. Sections include **Use Case Personas (`#personas`)**, **Custom Workflows (`#workflows`)**, **RAG Intelligence (`#rag`)**, and **Agentic VaaS (`#vaas`)**.
  * Embeds all 4 product demo MP4 videos inside styled dark wrappers with detailed bullet-point breakdowns of capabilities (e.g., automated document verification, multi-turn mock interviews with grading rubrics).
* **`src/app/use-cases/page.tsx` (`/use-cases`)**:
  * Vertical-specific marketing page focusing on **Higher Education Automation**. Sections detail the **MBA Admission Agent (`#mba`)**, **Mock Interviews Training (`#mock`)**, and **Assignments & Viva Evaluation Agent (`#viva`)**.
  * Features an active scroll-tracking sticky tab navigation bar that dynamically highlights the current category as the user scrolls down the page.
* **`src/app/product-video/page.tsx` (`/product-video`)**:
  * Dedicated theater-mode presentation screen designed for uninterrupted viewing of Alassatech's video demonstrations.
* **`src/app/privacy/page.tsx` & `src/app/terms/page.tsx` (`/privacy`, `/terms`)**:
  * Clean typography layouts displaying legal compliance, GDPR/data security practices, institutional data governance standards, and terms of service.

#### Shared Stylesheets (`src/app/assets/css/`)
* **`src/app/assets/css/index_core.css`**: The primary CSS foundation file imported globally. Defines all `:root` CSS design tokens, HTML/body resets, global typography rules, layout utilities (`.container`, `.btn`, `.btn-primary`, `.btn-outline`), scroll reveal base classes, and mobile media queries.
* **`src/app/assets/css/shared.css`**: Specialized stylesheet dedicated to global navigation and footer layouts:
  * Defines `.nav-has-nested` and `.nav-dropdown-nested-trigger` for multi-tier dropdown menus.
  * Implements an **invisible hover bridge (`::after` with width/height)** that fills the gap between a parent menu link and a popped-out submenu, preventing frustrating dropdown closures when the user moves their mouse.
  * Defines grid structures for `.footer-grid` (`1.5fr 1fr 1fr 1fr`), social icon hover glows, and vertical section labels.

#### Reusable UI Components (`src/components/`)
* **`src/components/Navbar.tsx` (Client Component)**:
  * Implements the site-wide navigation header (`#nav`).
  * **Desktop Menu**: Houses main navigation links (`Home`, `Products`, `Use Cases`, `Product Video`, `Contact`). Includes multi-level hover dropdowns for Products and Use Cases, allowing direct jumping to section anchors (`/products#rag`, `/use-cases#mock`, etc.).
  * **Mobile Menu Drawer**: Features an interactive hamburger toggle icon (`#navToggle`). When clicked, expands `#navMenu` with a smooth slide-down animation and full-width mobile navigation links.
  * **Dynamic Glassmorphism**: React component structure allows `ClientScripts.tsx` to manipulate classes on scroll without re-rendering React state.
* **`src/components/Footer.tsx` (Server Component)**:
  * Renders the comprehensive 4-column footer grid.
  * **Column 1 (Brand)**: Alassatech logo, corporate identity (`ALASSA TECHNOLOGY SOLUTIONS Pvt Ltd`), corporate office address (*Ecoworks, Modi Business Park, Thane West, India*), and LinkedIn social link.
  * **Column 2 (Platform)**: Navigation links to core technology suites.
  * **Column 3 (Verticals)**: Navigation links to Higher Education solutions.
  * **Column 4 (Contact Us)**: Direct email contact (`techadmin@alassatech.in`), direct "Request a Demo" button, and an interactive **WhatsApp Action Button (`.footer-wa-btn`)** linking to WhatsApp chat.
  * **Bottom Bar**: Copyright notice (`© 2025 Alassatech Pvt Ltd. All rights reserved.`) and legal quick links.
* **`src/components/ClientScripts.tsx` (Client Component `'use client'`)**:
  * The centralized DOM event listener wrapper. Uses `useEffect` and `usePathname` from Next.js navigation to execute client-side behaviors across route changes:
    1. **Navbar Scroll Shadow Engine**: Listens to `window.addEventListener('scroll')`. If `window.scrollY > 8`, toggles `.is-scrolled` on `#nav`, instantly morphing the navbar into a frosted glass pill.
    2. **Mobile Menu Auto-Close**: When `pathname` changes (user navigates to a new page or anchor), automatically closes the mobile drawer (`#navMenu`) and resets the hamburger toggle icon.
    3. **IntersectionObserver Scroll Reveals**: Initializes a high-performance `IntersectionObserver` with `threshold: 0.15`. Observers scan the document for any element with class `.reveal`. When an element scrolls into 15% of the viewport, the observer attaches class `.in-view`, triggering the vertical upward slide and fade-in CSS transition.
    4. **WhatsApp Floating Action Widget (`.wa-float`)**: Injects a fixed floating WhatsApp button in the bottom right corner (`bottom: 28px; right: 28px; z-index: 300`) with a pulsating green radar ring (`@keyframes wa-pulse`) and an expandable tooltip label (`Chat on WhatsApp`).

---

## 7. Responsive Breakpoint Architecture

The application is engineered with **fluid responsiveness**, ensuring a stunning user experience across giant desktop monitors, laptops, tablets, and mobile smartphones.

```
+----------------------------------------------------------------------------------------------------+
| RESPONSIVE BREAKPOINT GRID BEHAVIOR                                                                |
+----------------------------------------------------------------------------------------------------+
| Breakpoint         | Target Devices               | Architectural Layout Shifts                  |
+--------------------+------------------------------+----------------------------------------------+
| > 1150px           | Widescreen Desktops / 4K     | Full 1360px container, 55%/45% hero grid     |
| <= 1023px          | Tablets (Portrait) / Laptops | Hero shifts to single-column centered (1fr). |
|                    |                              | Steps section shifts from horizontal chain   |
|                    |                              | to vertical stacked cards with border top/bot|
|                    |                              | Footer grid shifts to 2-column wrap          |
| <= 767px           | Mobile Phones (Standard)     | Section vertical padding shrinks to 3.5rem   |
|                    |                              | Marquee section labels hide for clean scroll |
|                    |                              | Feature metrics bar stacks vertically (1fr)  |
|                    |                              | Value & Use Case grids become single column  |
|                    |                              | Footer shifts to single column stacked layout|
|                    |                              | WhatsApp floating text tooltip hides (icon only)|
| <= 479px           | Compact Mobile Phones        | Container padding shrinks to 1.125rem        |
|                    |                              | Hero actions & CTA buttons stretch 100% width|
+--------------------+------------------------------+----------------------------------------------+
```

---

## 8. Key Technical Workflows & Integrations

### Web3Forms Serverless Contact Pipeline
The contact page (`src/app/contact/page.tsx`) implements a modern **serverless email submission workflow** without requiring a Node.js SMTP server or API database route:

```
+-------------------+       +--------------------+       +-----------------------+       +---------------------+
| User Fills Form   | ----> | JS Intercepts      | ----> | JSON Payload Formed   | ----> | Async POST Request  |
| (Name, Email, etc)|       | (preventDefault)   |       | Object.fromEntries()  |       | api.web3forms.com   |
+-------------------+       +--------------------+       +-----------------------+       +---------------------+
                                      |                                                             |
                                      v                                                             v
                            +--------------------+                                       +---------------------+
                            | Disable Submit Btn |                                       | Receive JSON Result |
                            | Text -> 'Sending...'|                                       | (result.success)    |
                            +--------------------+                                       +---------------------+
                                                                                                    |
                                                       +--------------------------------------------+
                                                       |
                                                       +---> [IF SUCCESS]:
                                                       |     - Hide Form Container (.split-form-wrap)
                                                       |     - Reveal #success-message Card (Flex Center)
                                                       |
                                                       +---> [IF ERROR / FAILURE]:
                                                             - Re-enable Submit Button ('Send Message')
                                                             - Dynamically Inject #error-message Div
                                                             - Display Red Error Alert Banner
```

**Exact JavaScript Implementation inside `contact/page.tsx`**:
```javascript
async function submitContactForm(event) {
  event.preventDefault();
  const form = document.getElementById('contactForm');
  const btn = document.getElementById('submitBtn');
  const successMsg = document.getElementById('success-message');
  const errorMsg = document.getElementById('error-message');
  
  if (errorMsg) errorMsg.style.display = 'none';
  
  // 1. Engage Loading State
  btn.disabled = true;
  btn.innerHTML = 'Sending...';
  
  // 2. Serialize Form Data
  const formData = new FormData(form);
  const object = Object.fromEntries(formData);
  const json = JSON.stringify(object);
  
  try {
    // 3. Send Async POST to Web3Forms API
    const response = await fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json', 
        'Accept': 'application/json' 
      },
      body: json
    });
    const result = await response.json();
    
    // 4. Handle Response
    if (result.success) {
      form.closest('.split-form-wrap').style.display = 'none';
      successMsg.style.display = 'flex';
      successMsg.style.flexDirection = 'column';
      successMsg.style.alignItems = 'center';
      successMsg.style.textAlign = 'center';
    } else {
      throw new Error(result.message || 'Submission failed');
    }
  } catch (err) {
    // 5. Fallback Error Handling
    btn.disabled = false;
    btn.innerHTML = 'Send Message';
    const contactEmail = process.env.NEXT_PUBLIC_CONTACT_EMAIL || 'techadmin@alassatech.in';
    let errDiv = document.getElementById('error-message');
    if (!errDiv) {
      errDiv = document.createElement('div');
      errDiv.id = 'error-message';
      errDiv.style.cssText = 'background:#fef2f2;border:1px solid #fecaca;color:#dc2626;padding:0.875rem 1rem;border-radius:10px;font-size:0.875rem;margin-top:1rem;';
      form.appendChild(errDiv);
    }
    errDiv.textContent = `Something went wrong. Please try again or email us directly at ${contactEmail}`;
    errDiv.style.display = 'block';
  }
}
```

### IntersectionObserver Scroll Reveal Engine
To ensure high performance without jank on mobile devices, all entrance animations are managed by a single DOM Observer initialized in `ClientScripts.tsx`:
```javascript
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
      }
    });
  },
  { threshold: 0.15 } // Fires when 15% of the element is visible in viewport
);

document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
```

### Frosted Glassmorphism Navbar State
To create the signature translucent pill header:
```javascript
const nav = document.getElementById('nav');
const handleScroll = () => {
  if (nav) {
    nav.classList.toggle('is-scrolled', window.scrollY > 8);
  }
};
window.addEventListener('scroll', handleScroll, { passive: true });
```

---

## 9. Local Development, Build & Deployment Guide

This section is designed to make the project **100% deployment and production ready**. Follow these exact steps whether you are running locally or shipping to enterprise servers.

### Step-by-Step Onboarding for New Employees

#### Prerequisites
* **Node.js**: Version 18.17.0 or higher (Node 20+ LTS recommended).
* **Package Manager**: Standard `npm` (bundled with Node.js).
* **Git**: To clone and manage the codebase.

#### 1. Clone & Install Dependencies
Open your terminal and clone the repository:
```bash
git clone <your-repository-url>
cd alassa-nextjs
npm install
```
*This installs all required Next.js 15, React 19, and TypeScript dependencies.*

#### 2. Configure Local Environment
Create your local environment file by copying the defaults or creating `.env.local` directly in `alassa-nextjs/`:
```bash
cat << 'EOF' > .env.local
NEXT_PUBLIC_WEB3FORMS_ACCESS_KEY="a501397c-5a04-4c76-9a37-e25f3900f7df"
NEXT_PUBLIC_CONTACT_EMAIL="techadmin@alassatech.in"
NEXT_PUBLIC_WHATSAPP_NUMBER="919176664239"
NEXT_PUBLIC_SITE_URL="http://localhost:3000"
EOF
```

#### 3. Launch Development Server
Start the Next.js development server with Turbopack fast-refresh enabled:
```bash
npm run dev
```
Open your browser and navigate to **[http://localhost:3000](http://localhost:3000)**. Your development environment is now active and will live-reload on save!

---

### Production Build & Verification

Before committing changes or pushing to production, execute the verification suite to ensure zero type errors or broken routes:

```bash
# 1. Run strict TypeScript compilation check across all components
npx tsc --noEmit

# 2. Build the optimized production bundle (SSG static generation & SSR optimization)
npm run build

# 3. Test the production bundle locally
npm run start
```

When `npm run build` succeeds, Next.js generates static prerendered HTML for all routes (`/`, `/contact`, `/products`, `/use-cases`, `/product-video`, `/terms`, `/privacy`) ensuring instantaneous page loads and optimal SEO score.

---

### Deployment Instructions (Vercel & Docker/VPS)

Because Alassatech is built cleanly on the Next.js App Router without requiring external SQL databases or custom server backends, deploying to production is seamless:

#### Option 1: Vercel (Recommended Enterprise Cloud)
1. Push your repository to **GitHub / GitLab / Bitbucket**.
2. Log into **Vercel** and select **Add New Project** -> Import your repository.
3. In the **Environment Variables** settings panel, add:
   * `NEXT_PUBLIC_WEB3FORMS_ACCESS_KEY`: `a501397c-5a04-4c76-9a37-e25f3900f7df`
   * `NEXT_PUBLIC_CONTACT_EMAIL`: `techadmin@alassatech.in`
   * `NEXT_PUBLIC_WHATSAPP_NUMBER`: `919176664239`
   * `NEXT_PUBLIC_SITE_URL`: `https://your-production-domain.com`
4. Click **Deploy**. Vercel will automatically run `npm run build` and distribute the site to global edge CDNs with automatic SSL certificates.

#### Option 2: Self-Hosted VPS / Docker / AWS EC2
If deploying to an internal enterprise Linux server (Ubuntu / Debian / CentOS):
1. Install Node.js 20+ and PM2 process manager on the server:
   ```bash
   npm install -g pm2
   ```
2. Clone the repo onto the server, create your `.env.local` file with production values, and install dependencies:
   ```bash
   npm install --production=false
   ```
3. Build the production bundle:
   ```bash
   npm run build
   ```
4. Start the application as a background daemon using PM2:
   ```bash
   pm2 start npm --name "alassa-web" -- run start
   pm2 save
   pm2 startup
   ```
5. Configure your Nginx or Apache reverse proxy to forward traffic from port 80/443 to `http://localhost:3000`.

---

## 🏁 Conclusion
You now possess the **complete, production-ready architectural blueprint** of Alassa Technology Solutions. Every environment variable, color token, CSS rule, React component, animation observer, and API pipeline has been mapped. Welcome to the team, and happy coding! 🚀

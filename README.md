# Alassatech Web Application

## Tech Stack
- **Framework:** Next.js 15 (App Router)
- **UI:** React 19, TypeScript
- **Styling:** Vanilla CSS (`src/app/assets/css/index_core.css`)
- **Forms:** Web3Forms API

## Getting Started

### 1. Install Dependencies
```bash
npm install
```

### 2. Environment Setup
Copy the example environment file and configure your local variables:
```bash
cp .env.example .env.local
```

Required variables in `.env.local`:
```env
NEXT_PUBLIC_WEB3FORMS_ACCESS_KEY="your_web3forms_access_key_here"
NEXT_PUBLIC_CONTACT_EMAIL="contact@yourdomain.com"
NEXT_PUBLIC_WHATSAPP_NUMBER="1234567890"
NEXT_PUBLIC_SITE_URL="http://localhost:3000"
```

### 3. Run Development Server
```bash
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) in your browser.

## Available Scripts

- `npm run dev` – Starts the development server on port 3000.
- `npm run build` – Creates an optimized production build.
- `npm run start` – Serves the production build.
- `npx tsc --noEmit` – Runs TypeScript type checking.

## Architecture & File Structure

```text
alassa-nextjs/
├── public/assets/               # Static assets (MP4 demo videos, brand logos)
└── src/
    ├── app/                     # Next.js 15 App Router
    │   ├── layout.tsx           # Root wrapper (injects Navbar, Footer, & DOM scripts)
    │   ├── page.tsx             # Main Landing Page (/)
    │   ├── contact/page.tsx     # Contact Page + Web3Forms form submission (/contact)
    │   ├── products/page.tsx    # Products Suite (/products)
    │   ├── use-cases/page.tsx   # Industry Solutions (/use-cases)
    │   ├── product-video/       # Video Presentation Gallery (/product-video)
    │   ├── privacy/ & terms/    # Legal Compliance Pages (/privacy, /terms)
    │   └── assets/css/
    │       ├── index_core.css   # Core CSS design tokens (:root variables) & utilities
    │       └── shared.css       # Global navigation & footer layout styling
    └── components/              # Modular UI Components
        ├── Navbar.tsx           # Global header with multi-tier dropdowns & mobile drawer
        ├── Footer.tsx           # 4-column footer with contact links & WhatsApp CTA
        └── ClientScripts.tsx    # Client-side observers (scroll reveal, navbar glass state)
```

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

## Project Structure
- `public/assets/` – Static images and product demo videos (`.mp4`).
- `src/app/` – Next.js App Router pages and global CSS design tokens.
- `src/components/` – Reusable UI components (`Navbar`, `Footer`, `ClientScripts`).

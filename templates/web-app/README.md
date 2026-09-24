# Template: Web App

Next.js standalone com Vercel Functions. Sem servidor separado.

## Stack
- Next.js 15 + TypeScript + Tailwind + shadcn/ui
- Vercel Functions (API Routes) para lógica server-side
- Clerk para auth (opcional)
- Neon PostgreSQL (opcional)

## Setup
```bash
cp .env.example .env.local
pnpm install
pnpm dev  # http://localhost:3000
```

## Deploy
```bash
vercel --prod
```

# Template: SaaS

Template para produto SaaS completo. Criado pelo Vibecoder Hub.

## Stack
- **Frontend**: Next.js 15 + TypeScript + Tailwind + shadcn/ui
- **Auth**: Clerk
- **Backend**: FastAPI + Python 3.12 + uv
- **Database**: PostgreSQL + Prisma
- **Payments**: Stripe
- **Deploy**: Vercel + Railway

## Setup
```bash
cp .env.example .env.local    # Preencha com suas keys
pnpm install && uv sync
pnpm prisma migrate dev
pnpm dev                       # http://localhost:3000
uv run uvicorn src.main:app --reload  # http://localhost:8000
```

## Rotas
- `/` — Landing page (público)
- `/pricing` — Preços
- `/dashboard` — App (requer auth)
- `/dashboard/billing` — Gerenciar plano

## Sincronizar configs do hub
```bash
python ~/vibecoder-hub/scripts/sync-hub.py .
```

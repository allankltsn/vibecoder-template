# SaaS Template — Claude Code Instructions

## Tipo de projeto
Produto SaaS completo: landing page + app autenticado + backend API + banco de dados.

## Stack
- **Frontend**: Next.js 15, App Router, TypeScript, Tailwind CSS, shadcn/ui
- **Backend**: FastAPI, Python 3.12+, uv
- **Auth**: Clerk ou NextAuth.js
- **Database**: PostgreSQL + Prisma (TS) ou SQLModel (Python)
- **Payments**: Stripe
- **Deploy**: Vercel (web) + Railway/Render (api + db)

## Estrutura
```
.
├── apps/
│   ├── web/          # Next.js — landing + auth + dashboard
│   └── api/          # FastAPI — lógica de negócio + dados
├── .claude/          # Configs Claude Code
├── AGENTS.md         # Instruções para outros agentes
└── orca.yaml         # Orquestração Orca
```

## Fluxo de desenvolvimento SaaS

1. **Branding**: logo, cores, tipografia → salve em `apps/web/src/styles/brand.ts`
2. **Landing page**: `apps/web/src/app/(marketing)/`
3. **Auth**: configure Clerk ou NextAuth em `apps/web/src/app/(auth)/`
4. **Dashboard**: `apps/web/src/app/(app)/` — rotas protegidas
5. **API**: endpoints em `apps/api/src/routers/`
6. **Payments**: integração Stripe em `apps/api/src/services/billing.py`

## Variáveis de ambiente necessárias
Copie `.env.example` para `.env.local` e preencha:
- `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` + `CLERK_SECRET_KEY`
- `DATABASE_URL`
- `STRIPE_SECRET_KEY` + `STRIPE_WEBHOOK_SECRET`
- `ANTHROPIC_API_KEY` (se usar AI features)

## Regras
- Rotas de marketing (`/`, `/pricing`, `/blog`) ficam em `(marketing)/`
- Rotas do app autenticado ficam em `(app)/` com middleware de auth
- Nunca coloque lógica de negócio em Server Actions — use a API Python
- Tipagem end-to-end: tipos Pydantic → OpenAPI → TS via `openapi-typescript`

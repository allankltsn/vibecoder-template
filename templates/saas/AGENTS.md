# SaaS Template — Agent Instructions

## Visão geral
Produto SaaS completo. Stack: Next.js 15 (frontend + landing) + FastAPI (backend) + PostgreSQL.

## Mapa de responsabilidades

| Camada | Localização | Tecnologia |
|--------|-------------|------------|
| Landing/Marketing | apps/web/src/app/(marketing)/ | Next.js, Tailwind |
| App autenticado | apps/web/src/app/(app)/ | Next.js, Clerk |
| API REST | apps/api/src/routers/ | FastAPI |
| Lógica de negócio | apps/api/src/services/ | Python |
| Database | apps/api/src/db/ | SQLModel + PostgreSQL |
| Payments | apps/api/src/services/billing.py | Stripe Python SDK |

## Regras críticas

1. Auth é gerenciado pelo Clerk — não implemente auth custom
2. Rotas do app (`/dashboard`, `/settings`) exigem usuário autenticado via middleware
3. Dados sensíveis (keys, tokens) nunca no frontend — sempre via API
4. Stripe webhooks validados com `stripe.Webhook.construct_event()`
5. Use Prisma migrations para schema changes (nunca edite o DB direto)

## Padrão de feature SaaS

```
Nova feature: "user pode exportar dados"

1. apps/api/src/routers/exports.py  — endpoint POST /api/v1/exports
2. apps/api/src/services/export.py  — lógica de geração do arquivo
3. apps/web/src/app/(app)/exports/  — página do dashboard
4. apps/web/src/lib/exports.ts      — client para chamar a API
```

## Comandos
```bash
# Dev
pnpm dev          # frontend
uv run uvicorn src.main:app --reload  # backend

# Database
pnpm prisma migrate dev
pnpm prisma studio

# Deploy check
vercel build --prod
```

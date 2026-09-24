# SaaS — Agent Instructions

Stack: Next.js 15 + FastAPI + Clerk + Stripe + PostgreSQL.

## Mapa
| Camada | Localização |
|--------|-------------|
| Landing | apps/web/src/app/(marketing)/ |
| App auth | apps/web/src/app/(app)/ |
| API | apps/api/src/routers/ |
| Serviços | apps/api/src/services/ |
| DB | apps/api/src/db/ |

## Regras
1. Clerk gerencia toda autenticação
2. Dados sensíveis nunca no frontend
3. Stripe webhook com `stripe.Webhook.construct_event()`
4. Migrations via Prisma, nunca edite DB direto

# SaaS Template — Claude Code

Stack: Next.js 15 (frontend + landing) + FastAPI (backend) + PostgreSQL.

## Rotas
- `(marketing)/` — landing, pricing (público)
- `(auth)/` — sign-in, sign-up (Clerk)
- `(app)/` — dashboard e features (requer auth)

## Regras
- Auth via Clerk — não implemente auth custom
- Lógica de negócio na API Python, não em Server Actions
- Stripe webhooks validados com assinatura
- Types end-to-end: Pydantic → OpenAPI → TypeScript

## Comandos
```bash
pnpm dev                            # frontend
uv run uvicorn src.main:app --reload # backend
pnpm prisma studio                   # browser do DB
```

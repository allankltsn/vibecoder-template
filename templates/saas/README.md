# Template: SaaS

Template completo para produto SaaS com landing page, auth, dashboard e pagamentos.

## Stack

- **Frontend**: Next.js 15 + TypeScript + Tailwind + shadcn/ui
- **Auth**: Clerk
- **Backend**: FastAPI + Python 3.12 + uv
- **Database**: PostgreSQL + Prisma
- **Payments**: Stripe
- **Deploy**: Vercel + Railway

## Setup inicial

```bash
# 1. Clonar (via scaffold)
python ../../scripts/scaffold.py --template saas --name meu-produto

# 2. Instalar dependências
pnpm install
uv sync

# 3. Configurar ambiente
cp .env.example .env.local
# edite .env.local com suas keys

# 4. Database
pnpm prisma migrate dev

# 5. Dev
pnpm dev          # http://localhost:3000
uv run uvicorn src.main:app --reload  # http://localhost:8000
```

## Estrutura de rotas

```
/ ................. Landing page (público)
/pricing .......... Página de preços (público)
/sign-in .......... Login via Clerk
/sign-up .......... Cadastro via Clerk
/dashboard ........ App principal (requer auth)
/dashboard/settings Settings do usuário
/dashboard/billing  Gerenciar plano/pagamento
```

## Personalização do branding

Edite `apps/web/src/styles/brand.ts`:

```typescript
export const brand = {
  name: "Meu Produto",
  tagline: "O que seu produto faz",
  colors: {
    primary: "#6366f1",    // indigo
    secondary: "#8b5cf6",  // violet
  },
};
```

## Deploy

```bash
# Frontend (Vercel)
vercel --prod

# Backend (Railway)
railway up
```

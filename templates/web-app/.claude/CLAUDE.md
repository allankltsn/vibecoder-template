# Web App — Claude Code

Next.js 15 standalone. Backend via API Routes (Vercel Functions).

## Estrutura
- `src/app/(marketing)/` — páginas públicas
- `src/app/(app)/` — páginas com auth
- `src/app/api/` — API Routes / Vercel Functions
- `src/components/ui/` — shadcn/ui (não modifique)
- `src/components/features/` — seus componentes

## Regras
- Server Components por padrão, `"use client"` só quando necessário
- Route Handlers para webhooks e APIs públicas
- Server Actions para mutations de usuários autenticados
- Env vars privadas só em route handlers e server actions

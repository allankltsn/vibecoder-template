# Web App Template — Agent Instructions

## Visão geral
Web app Next.js standalone. Toda lógica server-side em API Routes ou Server Actions.
Deploy em Vercel, banco de dados opcional via Neon ou PlanetScale.

## Mapa de arquivos

```
src/app/api/           -> Vercel Functions (REST endpoints)
src/app/(marketing)/   -> Páginas públicas (/, /pricing, /about)
src/app/(app)/         -> Páginas autenticadas (/dashboard, /settings)
src/components/ui/     -> Componentes shadcn (não modifique)
src/components/features/ -> Componentes de domínio do seu app
src/lib/               -> Utilitários, clientes API, helpers
src/types/             -> TypeScript types e interfaces
```

## Regras

1. Server Components por padrão — `"use client"` apenas quando necessário
2. Dados do servidor via `fetch` em Server Components ou Server Actions
3. Variáveis de ambiente públicas: prefixo `NEXT_PUBLIC_`
4. Variáveis privadas (API keys): apenas em route handlers e server actions
5. Imagens: use `next/image` com `sizes` configurado
6. Fonts: use `next/font/google` no layout raiz

## Padrão de nova feature

```
1. Tipo de rota:
   - Pública (sem auth) → src/app/(marketing)/minha-pagina/page.tsx
   - Protegida (com auth) → src/app/(app)/minha-pagina/page.tsx

2. Se precisar de API:
   - src/app/api/minha-feature/route.ts (GET, POST, etc)
   - src/lib/minha-feature.ts (client para o frontend chamar)

3. Componentes:
   - src/components/features/minha-feature/MinhaFeature.tsx
```

## Comandos

```bash
# Adicionar componente shadcn
pnpm dlx shadcn@latest add button

# Type check
pnpm typecheck

# Lint
pnpm check
```

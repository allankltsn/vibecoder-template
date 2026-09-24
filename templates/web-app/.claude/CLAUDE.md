# Web App Template — Claude Code Instructions

## Tipo de projeto
Web app standalone com Next.js. Backend via Vercel Functions (API Routes).
Sem servidor Python separado — ideal para apps simples a médios.

## Stack
- **Next.js 15** com App Router + TypeScript
- **Tailwind CSS** + shadcn/ui
- **Vercel Functions** para lógica server-side (API Routes)
- **Prisma** + Neon/PlanetScale para banco (opcional)
- **Clerk** para auth (opcional)

## Estrutura
```
.
├── src/
│   ├── app/
│   │   ├── api/          # Vercel Functions (route handlers)
│   │   ├── (marketing)/  # Páginas públicas
│   │   └── (app)/        # Páginas autenticadas
│   ├── components/
│   │   ├── ui/           # shadcn/ui components
│   │   └── features/     # Componentes de domínio
│   ├── lib/
│   │   ├── api.ts        # Client para chamar as API routes
│   │   └── db.ts         # Cliente Prisma (se usar DB)
│   └── types/
├── public/
├── .claude/
├── AGENTS.md
└── orca.yaml
```

## Quando usar Vercel Functions vs Server Actions

- **Route Handler** (`app/api/*/route.ts`): chamadas de terceiros, webhooks, endpoints públicos
- **Server Action**: mutations do usuário autenticado, forms, operações simples
- Nunca misture: escolha um padrão por feature

## Comandos

```bash
pnpm dev           # http://localhost:3000
pnpm build         # build de produção
pnpm typecheck     # verificar tipos
vercel --prod      # deploy
```

# Vibecoder Monorepo — Claude Code Instructions

## Projeto
Monorepo Python + TypeScript gerenciado por Turborepo. Stack completa: Next.js 15 (web), FastAPI (api), pacotes compartilhados.

## Estrutura de apps
- `apps/web` — Frontend Next.js 15, App Router, TypeScript, Tailwind, shadcn/ui
- `apps/api` — Backend FastAPI, Python 3.12+, uv, Pydantic v2
- `packages/ui` — Componentes React reutilizáveis (base shadcn)
- `packages/config` — Configs compartilhadas (Biome, TypeScript, ESLint)
- `packages/ai` — Utilitários LLM/AI (chamadas Claude, OpenAI, embeddings)

## Convenções de código

### TypeScript / Next.js
- App Router com Server Components por padrão; Client Components apenas quando necessário
- Imports absolutos via `@/` (configurado em tsconfig.json)
- Biome para lint e format (não ESLint + Prettier separados)
- shadcn/ui para componentes — adicione via `pnpm dlx shadcn@latest add <component>`
- Zod para validação de schemas

### Python / FastAPI
- uv para gerenciar dependências (não pip direto)
- Ruff para lint e format
- Pydantic v2 para modelos e validação
- Typing explícito em toda função pública
- pytest para testes

## Comandos úteis

```bash
# Dev
pnpm dev                    # todos os apps
pnpm dev --filter=web       # só frontend
pnpm dev --filter=api       # só backend

# Qualidade
pnpm check                  # biome check + ruff check
pnpm fix                    # auto-fix lint issues

# Testes
pnpm test                   # todos os testes
pnpm test --filter=web      # só testes web

# Adicionar pacote
pnpm add <pkg> --filter=web         # no app web
pnpm add <pkg> --filter=packages/ui # em packages/ui
uv add <pkg>                        # python (na raiz)
```

## Workflow de features
1. Crie branch: `git checkout -b feat/nome-da-feature`
2. Implemente com TDD quando possível
3. Rode `pnpm check` antes de commitar
4. Commit com mensagem convencional: `feat(web): add user auth`
5. Abra PR com descrição clara do que e por quê

## Deploy
- Push para `main` → deploy automático na Vercel
- PRs → preview deployments automáticos
- API: configurar como Vercel Function ou Railway

## Regras importantes
- Nunca modifique arquivos em `packages/config` sem entender o impacto em todos os apps
- Tipos compartilhados ficam em `packages/ai/src/types/`
- Variáveis de ambiente: `.env.local` (local), `.env.example` (documentação)
- Secrets nunca no código — use Vercel Environment Variables

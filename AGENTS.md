# Vibecoder Monorepo — Agent Instructions

> Este arquivo instrui agentes de codificação (Codex, Gemini CLI, etc.) sobre como trabalhar neste repositório.

## Visão geral do projeto

Monorepo Python + TypeScript com Turborepo. Stack:
- `apps/web` — Next.js 15, TypeScript, App Router, Tailwind CSS, shadcn/ui
- `apps/api` — FastAPI, Python 3.12+, uv, Pydantic v2
- `packages/ui` — Componentes React reutilizáveis
- `packages/config` — Configurações compartilhadas
- `packages/ai` — Utilitários LLM compartilhados

## Regras obrigatórias

1. **Sempre rode lint antes de terminar** — `pnpm check` ou `ruff check .` (Python)
2. **Imports absolutos em TS** — use `@/` para imports dentro do mesmo app
3. **Types explícitos** — sem `any` em TypeScript, sem funções sem type hints em Python
4. **Server Components por padrão** — adicione `"use client"` apenas quando necessário
5. **Variáveis de ambiente** — leia de `process.env` (TS) ou `os.environ` / `pydantic-settings` (Python)
6. **Nunca commite .env** — apenas `.env.example` vai para o repositório

## Estrutura de arquivos por feature

Para cada feature nova, siga este padrão:

```
apps/web/src/
  app/(feature-name)/
    page.tsx          # Server Component (rota)
    components/
      FeatureName.tsx # Client Component se precisar de interatividade
  lib/
    feature-name.ts   # Lógica / fetching / server actions
  types/
    feature-name.ts   # Tipos TypeScript

apps/api/src/
  routers/
    feature_name.py   # FastAPI router
  services/
    feature_name.py   # Lógica de negócio
  models/
    feature_name.py   # Pydantic models
  tests/
    test_feature_name.py
```

## Comandos de referência

```bash
# Instalar dependência TS em app específico
pnpm add <pacote> --filter=web

# Instalar dependência Python
uv add <pacote>

# Adicionar componente shadcn
pnpm dlx shadcn@latest add <componente> --cwd apps/web

# Rodar testes
pnpm test --filter=web
cd apps/api && uv run pytest

# Verificar build
pnpm build
```

## Padrões de API

### Endpoints FastAPI
- Prefixo: `/api/v1/`
- Autenticação via header `Authorization: Bearer <token>`
- Respostas em JSON com campo `data`, `error`, `meta`
- HTTP status codes semânticos

### Server Actions (Next.js)
- Arquivos terminando em `.action.ts`
- Validação com Zod antes de qualquer lógica
- Retorno tipado: `{ success: true, data: T } | { success: false, error: string }`

## Padrão de commit

```
tipo(escopo): descrição curta

Tipos: feat | fix | refactor | test | docs | chore | style
Exemplos:
  feat(web): add user authentication flow
  fix(api): handle null user_id in profile endpoint
  refactor(packages/ai): simplify LLM client interface
```

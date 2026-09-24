# Vibecoder Template — Option A: Monorepo

> Stack Python + TypeScript unificada num único repositório gerenciado por **Turborepo**.
> Agentes AI (Claude Code, Codex, Orca) enxergam o repo inteiro e colaboram em todos os apps.

## Estrutura

```
vibecoder-template/
├── apps/
│   ├── web/          # Next.js 15 + TypeScript + Tailwind + shadcn/ui
│   └── api/          # FastAPI + Python 3.12 + uv
├── packages/
│   ├── ui/           # Componentes compartilhados (shadcn/ui base)
│   ├── config/       # ESLint, TypeScript, Biome configs
│   └── ai/           # Utilitários AI/LLM compartilhados
├── .claude/
│   ├── CLAUDE.md     # Instruções para Claude Code
│   ├── settings.json # Configurações e agentes Claude Code
│   └── agents/       # Subagentes especializados
├── AGENTS.md         # Instruções para Codex / outros agentes
├── orca.yaml         # Orquestração Orca (multi-agent)
├── turbo.json        # Pipeline Turborepo
├── package.json      # Root workspace
├── pnpm-workspace.yaml
└── pyproject.toml    # Python workspace
```

## Quando usar esta opção

✅ Projetos com frontend + backend fortemente acoplados  
✅ Time pequeno (1-3 devs) que quer tudo num lugar  
✅ Compartilhamento de tipos TypeScript entre web e api  
⚠️ Projetos comerciais separados ficam misturados com tooling interno  

## Quick Start

```bash
# Instalar dependências (Node)
pnpm install

# Instalar dependências (Python)
uv sync

# Rodar todos os apps em dev
pnpm dev

# Rodar apenas o web
pnpm dev --filter=web

# Rodar apenas a api
pnpm dev --filter=api

# Build todos
pnpm build

# Lint + format
pnpm check
```

## AI Workflow

```bash
# Claude Code — abre o workspace inteiro
claude .

# Codex — contexto do monorepo completo (via AGENTS.md)
codex "implement feature X"

# Orca — orquestra Claude + Codex + Gemini em paralelo
orca run --profile feature --task "implement user authentication"
```

## Deploy

- **Web:** Vercel (auto-detect Next.js em `apps/web`)
- **API:** Vercel Functions ou Railway
- **CI:** GitHub Actions (`.github/workflows/ci.yml`)

## Stack

| Camada | Tecnologia |
|--------|-----------|
| Frontend | Next.js 15, TypeScript, Tailwind CSS, shadcn/ui |
| Backend | FastAPI, Python 3.12+, uv, Pydantic v2 |
| Linting | Biome (TS), Ruff (Python) |
| Monorepo | Turborepo + pnpm workspaces |
| Deploy | Vercel + Vercel Functions |
| AI Tools | Claude Code, Codex, Orca |

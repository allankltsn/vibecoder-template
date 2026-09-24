# Vibecoder Hub — Option C: Hub + Satellite

> O **Hub** é o coração do seu workflow de desenvolvimento AI-assistido.
> Aqui vivem seus agentes configurados, templates reutilizáveis, workflows Orca
> e scripts de automação. Cada projeto que você cria é um **satélite** que nasce
> do hub e herda suas configurações.

## Como funciona

```
vibecoder-hub/           ← ESTE REPOSITÓRIO (hub)
  .claude/               ← Configs globais Claude Code
  orca/                  ← Workflows Orca reutilizáveis
  templates/             ← Base para novos projetos
  scripts/               ← Automações (scaffold, sync, status)
  docs/                  ← Guias de workflow

~/projetos/              ← Seus projetos satélite
  meu-saas/              ← criado via: python scripts/new-project.py saas meu-saas
  meu-agente/            ← criado via: python scripts/new-project.py ai-agent meu-agente
  minha-cli/             ← criado via: python scripts/new-project.py cli-tool minha-cli
```

## Quick Start

```bash
# 1. Clonar o hub
git clone https://github.com/allankltsn/vibecoder-template.git ~/vibecoder-hub
cd ~/vibecoder-hub

# 2. Ver projetos ativos
python scripts/status.py

# 3. Criar novo projeto SaaS
python scripts/new-project.py saas meu-produto ~/projetos/

# 4. Criar agente AI
python scripts/new-project.py ai-agent meu-agente ~/projetos/

# 5. Sincronizar configs do hub para projetos existentes
python scripts/sync-hub.py ~/projetos/meu-produto
```

## Documentação

| Documento | Conteúdo |
|-----------|---------|
| [docs/workflow.md](docs/workflow.md) | Workflow completo do branding ao deploy |
| [docs/agents.md](docs/agents.md) | Catálogo de agentes e quando usar cada um |
| [docs/orca-guide.md](docs/orca-guide.md) | Guia completo do Orca |
| [docs/branding-to-deploy.md](docs/branding-to-deploy.md) | Guia passo a passo |

## Estrutura completa

```
.
├── .claude/
│   ├── CLAUDE.md          # Instruções globais Claude Code
│   ├── settings.json      # Config Claude Code
│   └── agents/            # Subagentes especializados
│       ├── architect.md
│       ├── fullstack-dev.md
│       ├── ai-engineer.md
│       ├── qa-engineer.md
│       ├── deployer.md
│       └── content-writer.md
├── AGENTS.md              # Instruções globais para Codex
├── orca/
│   ├── orca.yaml          # Config Orca master
│   └── profiles/          # Perfis reutilizáveis
│       ├── feature.yaml
│       ├── bugfix.yaml
│       └── review.yaml
├── templates/
│   ├── saas/
│   ├── web-app/
│   ├── ai-agent/
│   └── cli-tool/
├── scripts/
│   ├── new-project.py     # Scaffold de projetos
│   ├── sync-hub.py        # Sync configs hub → projeto
│   └── status.py          # Overview de projetos ativos
└── docs/
    ├── workflow.md
    ├── agents.md
    ├── orca-guide.md
    └── branding-to-deploy.md
```

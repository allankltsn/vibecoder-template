# Vibecoder Hub — Claude Code Master Instructions

## O que é este repositório

Este é o **Hub central** do seu workflow de desenvolvimento AI-assistido.
Não é um projeto para usuários finais — é a infraestrutura interna que alimenta
todos os seus projetos satélite.

## Estrutura do Hub

```
.claude/agents/    Subagentes Claude especializados — invoque por nome
orca/              Configs Orca para orquestrar múltiplos agentes
templates/         Templates de projeto (saas, web-app, ai-agent, cli-tool)
scripts/           Automações Python (scaffold, sync, status)
docs/              Documentação de workflow (leia docs/workflow.md)
```

## Subagentes disponíveis

Invoque pelo nome em qualquer projeto:

| Agente | Quando usar |
|--------|-------------|
| `architect` | Decisões de arquitetura, design de sistema |
| `fullstack-dev` | Features com frontend + backend |
| `ai-engineer` | Agentes, tools, pipelines LLM |
| `qa-engineer` | Testes, revisão de qualidade |
| `deployer` | CI/CD, Vercel, Docker, infra |
| `content-writer` | Copy, docs, README, changelogs |

## Comandos do Hub

```bash
# Criar novo projeto
python scripts/new-project.py <tipo> <nome> [diretório-saída]

# Ver status de projetos ativos
python scripts/status.py

# Sincronizar configs do hub para um projeto
python scripts/sync-hub.py <caminho-do-projeto>

# Orquestrar com Orca
orca run --config orca/orca.yaml --profile feature --task "..."
```

## Quando trabalhar aqui vs num satélite

**Trabalhe no Hub quando:**
- Atualizar instruções de subagentes (`.claude/agents/`)
- Melhorar templates de projeto
- Criar novos perfis Orca
- Atualizar scripts de automação

**Trabalhe no satélite quando:**
- Desenvolver features do produto
- Corrigir bugs
- Escrever testes

## Regras deste repositório

1. Mude templates com cuidado — afetam projetos futuros
2. Documente qualquer mudança em `docs/workflow.md`
3. Scripts em `scripts/` devem funcionar sem dependências externas além da stdlib Python
4. Perfis Orca são documentados em `docs/orca-guide.md`

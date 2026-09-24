# Catálogo de Agentes — Quando Usar Cada Um

## Subagentes Claude Code (`.claude/agents/`)

Invoque dentro do Claude Code com: `use <nome>: <tarefa>`

### `architect`
**Quando usar:** Antes de qualquer feature não-trivial. Antes de mudar interfaces compartilhadas.  
**Output:** Decisão de design documentada com trade-offs.  
**Exemplo:** `use architect: projete a estrutura de multi-tenancy para o banco de dados`

### `fullstack-dev`
**Quando usar:** Features que cruzam frontend e backend.  
**Output:** Implementação completa do endpoint até o componente React.  
**Exemplo:** `use fullstack-dev: implemente o upload de avatar do usuário`

### `ai-engineer`
**Quando usar:** Qualquer feature envolvendo LLMs, agentes, embeddings, RAG.  
**Output:** Implementação com atenção a custo, latência e observabilidade.  
**Exemplo:** `use ai-engineer: crie um agente que resume tickets de suporte`

### `qa-engineer`
**Quando usar:** Após implementar qualquer feature. Antes de abrir PR.  
**Output:** Testes escritos + lista de edge cases cobertos.  
**Exemplo:** `use qa-engineer: escreva testes para o endpoint POST /api/v1/payments`

### `deployer`
**Quando usar:** Setup inicial de CI/CD, problemas de deploy, gestão de env vars.  
**Output:** Configuração funcional de deploy.  
**Exemplo:** `use deployer: configure o deploy automático na Vercel para este projeto`

### `content-writer`
**Quando usar:** Landing page, README, changelogs, mensagens de erro, copy de UI.  
**Output:** Texto claro, direto e orientado a ação.  
**Exemplo:** `use content-writer: escreva o hero section da landing page do produto`

---

## Agentes Orca (via `orca run --profile`)

Rodados via CLI, paralelamente, com comparação de resultados.

| Perfil | Agentes | Estratégia | Quando |
|--------|---------|-----------|--------|
| `feature` | Claude + Codex | Paralelo + julgamento Claude | Feature importante |
| `bugfix` | Claude + Codex | Paralelo + 2 rounds | Bug complexo |
| `review` | Claude | Sequencial | Antes do PR |
| `explore` | Claude + Codex + Gemini | Paralelo | Decisão de arquitetura |
| `ai-feature` | Claude | Sequencial | Feature LLM/AI |
| `quick` | Codex | Sequencial | Boilerplate rápido |

---

## Codex (direto, sem Orca)

Use para tasks simples e isoladas onde o contexto não é crítico.

```bash
codex "add TypeScript types to src/types/user.ts"
codex "write a Python function that validates email format"
codex "fix the typo in the error message on line 42 of src/lib/auth.ts"
```

---

## Escolhendo o agente certo

```
É uma decisão de design?
  → architect

Cruza frontend + backend?
  → fullstack-dev (interativo) ou Orca feature (comparativo)

Envolve LLM/AI?
  → ai-engineer

É copy/docs/conteúdo?
  → content-writer

É infra/deploy/CI?
  → deployer

Precisa de testes?
  → qa-engineer

É bugfix complexo?
  → Orca bugfix

É boilerplate rápido?
  → Codex direto ou Orca quick
```

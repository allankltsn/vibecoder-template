# Guia Orca — Orquestração Multi-Agente

Orca roda múltiplos agentes AI em paralelo para a mesma tarefa e permite escolher
o melhor resultado. Ideal para features importantes onde você quer mais de uma perspectiva.

## Instalação

```bash
# Instalar Orca
pip install orca-ai   # ou via brew/npm conforme o método oficial

# Verificar instalação
orca --version
```

## Conceitos fundamentais

| Conceito | Descrição |
|---------|-----------|
| **Agente** | Um modelo LLM específico (claude, codex, gemini) |
| **Perfil** | Configuração de quais agentes usar + estratégia |
| **Estratégia** | `parallel` (roda todos ao mesmo tempo) ou `sequential` |
| **Judge** | Agente que avalia os resultados e escolhe o melhor |
| **Round** | Uma rodada de execução (bugfix pode ter até 2 rounds) |

## Uso básico

```bash
# Rodar com perfil pré-definido do hub
orca run --config orca/orca.yaml --profile feature \
  --task "implement user profile settings page"

# Ver resultados lado a lado
orca diff

# Aplicar o resultado escolhido
orca apply --winner claude  # ou codex, ou gemini

# Histórico de execuções
orca history
```

## Perfis disponíveis

### `feature` — Nova feature
Roda Claude + Codex em paralelo. Claude julga o melhor resultado.
Ideal para: páginas novas, endpoints, features verticais completas.

```bash
orca run --profile feature --task "add user avatar upload to settings page"
```

### `bugfix` — Corrigir bug
Roda Claude + Codex. Permite até 2 rounds de refinamento.
Ideal para: bugs com causa raiz não óbvia, regressões.

```bash
orca run --profile bugfix --task "fix 422 error when submitting form with special chars"
```

### `review` — Code review
Apenas Claude. Revisa qualidade, segurança, tipos.
Ideal para: antes de fazer PR, após uma feature grande.

```bash
orca run --profile review --task "review changes in apps/web/src/app/(app)/billing/"
```

### `explore` — Explorar opções
Roda Claude + Codex + Gemini. Máxima diversidade.
Ideal para: decisões de arquitetura, explorar abordagens diferentes.

```bash
orca run --profile explore --task "how should we implement real-time notifications?"
```

### `quick` — Task rápida
Apenas Codex. Sem julgamento.
Ideal para: boilerplate, renomear variáveis, pequenas mudanças.

```bash
orca run --profile quick --task "add missing TypeScript return types to lib/users.ts"
```

## Quando usar Orca vs Claude Code direto

**Use Orca quando:**
- A feature é importante e você quer mais de uma perspectiva
- Está corrigindo um bug complexo e não tem certeza da causa raiz
- Quer validar uma abordagem antes de implementar
- Tem tempo para comparar resultados

**Use Claude Code quando:**
- Está em modo interativo e iterando rápido
- Precisa de contexto profundo do projeto (muitos arquivos)
- A task é simples e não precisa de comparação
- Quer usar subagentes especializados (`architect`, `qa-engineer`, etc.)

## Dicas de produtividade

```bash
# Salvar tarefa frequente como alias
alias orca-feature="orca run --config ~/vibecoder-hub/orca/orca.yaml --profile feature"
orca-feature --task "..."

# Reutilizar última task
orca rerun

# Combinar partes de diferentes agentes
orca merge --take-frontend=codex --take-backend=claude
```

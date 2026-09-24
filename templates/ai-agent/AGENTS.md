# AI Agent — Agent Instructions

## Estrutura
- `agents/` — orquestração (não tem lógica de negócio)
- `tools/` — capacidades (testáveis isoladamente)
- `memory/` — persistência de contexto

## Regras
1. Cada tool: 1 responsabilidade, docstring clara
2. Timeout em todas as tools (30s máximo)
3. Rate limiting em APIs externas
4. Logs estruturados de cada ação
5. Nunca armazene dados sensíveis do usuário sem consentimento

# AI Agent — Claude Code

Agente AI com Agno + Claude. Tools customizadas, memória opcional.

## Estrutura
- `agents/` — definição e orquestração de agentes
- `tools/` — capacidades externas (1 arquivo = 1 tool)
- `memory/` — persistência de contexto
- `api/` — FastAPI wrapper (opcional)

## Padrão
- Tools são funções simples com docstring clara
- Teste cada tool independentemente
- Logs de cada LLM call para debug
- Timeout em todas as tools (máx 30s)

## Comandos
```bash
uv run python main.py          # interativo
uv run pytest tests/ -v        # testes
uv run uvicorn api.main:app    # com API
```

# Template: AI Agent

Agente AI com Agno + Claude. Ferramentas prontas, memória opcional, API REST opcional.

## Setup
```bash
uv sync
cp .env.example .env
# Adicione ANTHROPIC_API_KEY
uv run python main.py
```

## Adicionar tool
```python
# tools/minha_tool.py
from agno.tools import tool

@tool
def minha_tool(query: str) -> str:
    """Descrição para o LLM saber quando usar."""
    ...
```

Registre em `tools/__init__.py`.

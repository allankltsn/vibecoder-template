# Template: AI Agent

Template para agente AI autônomo usando Agno + Claude. Pronto para rodar localmente,
adicionar tools e expor via API.

## Setup

```bash
# Instalar dependências
uv sync

# Configurar ambiente
cp .env.example .env
# adicione ANTHROPIC_API_KEY=sk-ant-...

# Rodar agente interativo
uv run python main.py

# Com API REST
uv add fastapi uvicorn
uv run uvicorn api.main:app --reload
```

## Adicionar uma nova tool

```python
# tools/minha_tool.py
from agno.tools import tool

@tool
def minha_tool(parametro: str) -> str:
    """Descrição: o que faz e quando usar."""
    # implementação
    return resultado
```

Registre em `tools/__init__.py`:
```python
from .minha_tool import minha_tool

def get_all_tools():
    return [web_search_tool, minha_tool]
```

## Frameworks alternativos

Substitua Agno por LangChain ou CrewAI conforme o caso:

```bash
# LangChain
uv add langchain langchain-anthropic

# CrewAI
uv add crewai
```

## Deploy

- **API simples**: Railway ou Render com Dockerfile
- **Agente serverless**: AWS Lambda + Mangum
- **Workers de longa duração**: Modal ou Fly.io

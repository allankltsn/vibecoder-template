# AI Agent Template — Claude Code Instructions

## Tipo de projeto
Agente AI autônomo ou assistente conversacional. Frameworks suportados: LangChain, Agno, CrewAI.

## Stack
- **Python 3.12+** com uv
- **LangChain** ou **Agno** para orquestração de agentes
- **FastAPI** para expor o agente via API (opcional)
- **Redis** para memória/cache de conversas (opcional)
- **Anthropic Claude** como LLM principal

## Estrutura
```
.
├── agents/           # Definição dos agentes
│   ├── __init__.py
│   ├── base.py       # Agente base com configuração comum
│   └── specialized/  # Agentes especializados por domínio
├── tools/            # Tools customizadas para os agentes
│   ├── __init__.py
│   └── web_search.py
├── memory/           # Implementações de memória
│   └── redis_memory.py
├── api/              # FastAPI wrapper (opcional)
│   └── main.py
├── tests/
├── pyproject.toml
└── main.py           # Entry point
```

## Padrões de desenvolvimento

### Definição de agente (Agno)
```python
from agno.agent import Agent
from agno.models.anthropic import Claude

agent = Agent(
    model=Claude(id="claude-opus-4-5"),
    tools=[...],
    instructions="...",
    markdown=True,
)
```

### Definição de tool
```python
from langchain.tools import BaseTool
from pydantic import BaseModel, Field

class MyTool(BaseTool):
    name = "my_tool"
    description = "Faz X quando Y"
    
    def _run(self, query: str) -> str:
        ...
```

## Comandos
```bash
# Rodar agente interativo
uv run python main.py

# Rodar com API
uv run uvicorn api.main:app --reload

# Testes
uv run pytest tests/ -v
```

## Debug de agentes
- Ative verbose no LangChain: `LANGCHAIN_VERBOSE=true`
- Use `langchain-tracer` ou `LangSmith` para observabilidade
- Logs estruturados em `logs/agent.jsonl`

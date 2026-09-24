# AI Agent Template — Agent Instructions

## Visão geral
Projeto de agente AI com LangChain ou Agno. O agente usa Claude como LLM principal
e pode ter tools customizadas, memória e capacidade de orquestrar sub-agentes.

## Estrutura de responsabilidades

```
agents/       -> Lógica de orquestração e tomada de decisão
tools/        -> Capacidades externas do agente (busca, código, APIs)
memory/       -> Persistência de contexto entre conversas
api/          -> Interface HTTP para o agente (se necessário)
tests/        -> Testes unitários e de integração
```

## Regras

1. Cada tool tem um propósito único e bem definido
2. Tools são testáveis independentemente do agente
3. Nunca armazene dados do usuário sem consentimento explícito
4. Rate limiting em todas as chamadas a APIs externas
5. Timeouts em todas as tools (máximo 30s por tool call)
6. Logs estruturados de cada ação do agente (para debug)

## Padrão de nova tool

```python
# tools/minha_tool.py
from typing import Optional
from pydantic import BaseModel, Field

class MinhaToolInput(BaseModel):
    query: str = Field(description="O que pesquisar")
    max_results: int = Field(default=5, description="Número máximo de resultados")

def minha_tool(input: MinhaToolInput) -> str:
    """Descrição clara do que a tool faz e quando usá-la."""
    # implementação
    ...
```

## Padrão de teste

```python
# tests/test_tools.py
def test_minha_tool_retorna_resultado():
    result = minha_tool(MinhaToolInput(query="teste"))
    assert result is not None
    assert len(result) > 0

def test_minha_tool_timeout():
    # tool deve respeitar timeout de 30s
    import time
    start = time.time()
    minha_tool(MinhaToolInput(query="query longa"))
    assert time.time() - start < 30
```

## Comandos úteis

```bash
# Instalar dependências
uv add langchain anthropic agno

# Rodar agente
uv run python main.py --verbose

# Rodar testes
uv run pytest tests/ -v --tb=short
```

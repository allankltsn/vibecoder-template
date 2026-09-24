from agno.agent import Agent
from agno.models.anthropic import Claude

from tools import get_all_tools


def create_agent(model_id: str = "claude-opus-4-5") -> Agent:
    """Cria e configura o agente principal."""
    return Agent(
        model=Claude(id=model_id),
        tools=get_all_tools(),
        instructions=[
            "Você é um assistente útil e preciso.",
            "Quando não souber algo, diga claramente.",
            "Use as tools disponíveis quando necessário.",
            "Responda em português do Brasil.",
        ],
        markdown=True,
        show_tool_calls=True,
    )

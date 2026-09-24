"""Tool de exemplo: busca web via DuckDuckGo (sem API key)."""

from agno.tools import tool


@tool
def web_search_tool(query: str, max_results: int = 5) -> str:
    """Busca informações na web. Use quando precisar de dados recentes ou específicos.

    Args:
        query: O que pesquisar
        max_results: Número máximo de resultados (default: 5)
    """
    try:
        from duckduckgo_search import DDGS
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=max_results):
                results.append(f"- {r['title']}: {r['body']}")
        return "\n".join(results) if results else "Nenhum resultado encontrado."
    except ImportError:
        return "Instale duckduckgo-search: uv add duckduckgo-search"

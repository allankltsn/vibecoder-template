"""Lógica principal da CLI — sem dependência de Typer ou Rich."""

from pathlib import Path


def processar(entrada: str, verbose: bool = False) -> str:
    """Processa a entrada e retorna o resultado.

    Args:
        entrada: Caminho do arquivo ou texto direto
        verbose: Se True, inclui informações adicionais no output

    Returns:
        String com o resultado processado

    Raises:
        FileNotFoundError: Se entrada for um caminho de arquivo inexistente
    """
    path = Path(entrada)
    if path.exists():
        content = path.read_text(encoding="utf-8")
    else:
        content = entrada

    resultado = content.upper()  # substitua pela sua lógica

    if verbose:
        return f"[Input: {len(content)} chars]\n{resultado}"
    return resultado

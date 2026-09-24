# CLI Tool Template — Claude Code Instructions

## Tipo de projeto
Ferramenta CLI distribuível em Python. Usa Typer para interface, Rich para output bonito,
e é empacotada via uv para distribuição via pip/pipx.

## Stack
- **Python 3.12+** com uv
- **Typer** para CLI (baseado em Click com type hints)
- **Rich** para output formatado (tabelas, progresso, cores)
- **Pydantic** para configuração e validação
- **pytest** para testes

## Estrutura
```
.
├── src/
│   └── {package_name}/
│       ├── __init__.py
│       ├── cli.py         # Entry points Typer
│       ├── core.py        # Lógica principal
│       ├── config.py      # Configurações (pydantic-settings)
│       └── utils.py       # Utilitários
├── tests/
├── pyproject.toml         # Inclui [project.scripts] para o comando
└── README.md
```

## Padrão de comando Typer

```python
import typer
from rich.console import Console

app = typer.Typer(help="Descrição da CLI")
console = Console()

@app.command()
def processar(
    arquivo: str = typer.Argument(help="Arquivo a processar"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Processa o arquivo e gera output."""
    with console.status("Processando..."):
        resultado = core.processar(arquivo)
    console.print(f"[green]✓[/green] {resultado}")
```

## Comandos de desenvolvimento

```bash
# Instalar em modo dev (cria o comando localmente)
uv run pip install -e .

# Testar o comando
{comando} --help

# Rodar testes
uv run pytest tests/ -v

# Build para distribuição
uv build
```

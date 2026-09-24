# Template: CLI Tool

Ferramenta CLI Python distribuível via pip/pipx.

## Stack
- Python 3.12+ + uv
- Typer (CLI) + Rich (output)

## Setup
```bash
uv sync
uv run pip install -e .
mycli --help
```

## Adicionar comando
```python
# src/mycli/cli.py
@app.command()
def meu_comando(arg: str = typer.Argument()) -> None:
    """Descrição do comando."""
    ...
```

## Distribuir
```bash
uv build
uv publish
# Usuário final: pipx install mycli
```

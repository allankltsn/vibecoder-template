# CLI Tool Template — Agent Instructions

## Visão geral
Ferramenta CLI Python distribuível. Entry point definido em `pyproject.toml [project.scripts]`.

## Estrutura

```
src/{package}/
  cli.py      # Comandos Typer (interface do usuário)
  core.py     # Lógica de negócio (testável sem CLI)
  config.py   # Settings via pydantic-settings ou ~/.config/
  utils.py    # Helpers reutilizáveis
tests/
  test_core.py    # Testes da lógica (não da CLI)
  test_cli.py     # Testes da CLI via CliRunner
```

## Regras

1. **Separe CLI da lógica**: `cli.py` apenas lida com input/output; `core.py` tem a lógica
2. **Mensagens de erro claras**: use `console.print("[red]Erro:[/red] ...")` + `raise typer.Exit(1)`
3. **Progress feedback**: operações longas usam `console.status()` ou `Progress`
4. **Config persiste**: preferências do usuário em `~/.config/{tool}/config.toml`
5. **Exit codes corretos**: 0 = sucesso, 1 = erro de usuário, 2 = erro interno

## Padrão de teste CLI

```python
from typer.testing import CliRunner
from src.mypkg.cli import app

runner = CliRunner()

def test_comando_sucesso():
    result = runner.invoke(app, ["meu-comando", "arg"])
    assert result.exit_code == 0
    assert "esperado" in result.output

def test_comando_arquivo_invalido():
    result = runner.invoke(app, ["meu-comando", "nao-existe.txt"])
    assert result.exit_code == 1
```

## Distribuição

```bash
# Build
uv build

# Publicar no PyPI
uv publish

# Instalar via pipx (usuário final)
pipx install {package-name}
```

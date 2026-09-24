# CLI Tool — Claude Code

Python CLI com Typer + Rich. Distribuível via pip/pipx.

## Estrutura
- `src/mycli/cli.py` — comandos Typer
- `src/mycli/core.py` — lógica (sem dependência de Typer)
- `tests/` — testes via CliRunner

## Regras
- CLI e lógica separadas (core.py testável sem CLI)
- Mensagens de erro com `console.print("[red]Erro:[/red] ...")`
- Exit code 0 = sucesso, 1 = erro de usuário, 2 = erro interno
- Operações longas: `console.status("...")`

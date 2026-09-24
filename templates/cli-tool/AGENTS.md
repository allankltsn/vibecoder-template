# CLI Tool — Agent Instructions

Python CLI com Typer. Lógica separada da interface.

## Estrutura
- `cli.py` — interface (Typer, input/output)
- `core.py` — lógica de negócio (sem CLI)
- `tests/test_cli.py` — testes via CliRunner
- `tests/test_core.py` — testes unitários

## Regras
1. `core.py` nunca importa Typer ou Rich
2. Exit codes: 0 sucesso, 1 erro usuário, 2 erro interno
3. Mensagens de erro em vermelho via Rich
4. Teste CLI com `typer.testing.CliRunner`

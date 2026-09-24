import typer
from rich.console import Console

from . import __version__
from .core import processar

app = typer.Typer(
    name="mycli",
    help="Descrição da sua ferramenta CLI",
    no_args_is_help=True,
)
console = Console()


def version_callback(value: bool) -> None:
    if value:
        console.print(f"mycli versão {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None, "--version", "-V", callback=version_callback, is_eager=True
    ),
) -> None:
    """mycli — sua ferramenta CLI."""


@app.command()
def run(
    entrada: str = typer.Argument(help="Arquivo ou texto de entrada"),
    saida: str = typer.Option(None, "--output", "-o", help="Arquivo de saída"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Output detalhado"),
) -> None:
    """Processa a entrada e gera resultado."""
    with console.status(f"[bold green]Processando {entrada}...[/bold green]"):
        try:
            resultado = processar(entrada, verbose=verbose)
        except FileNotFoundError:
            console.print(f"[red]Erro:[/red] Arquivo '{entrada}' não encontrado.")
            raise typer.Exit(1)

    if saida:
        with open(saida, "w") as f:
            f.write(resultado)
        console.print(f"[green]✓[/green] Salvo em {saida}")
    else:
        console.print(resultado)

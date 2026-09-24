#!/usr/bin/env python3
"""Scaffold: cria um novo projeto a partir de um template Vibecoder."""

import argparse
import shutil
import sys
from pathlib import Path
from datetime import datetime

TEMPLATES_DIR = Path(__file__).parent.parent / "templates"
AVAILABLE_TEMPLATES = {
    "saas": "Produto SaaS completo (Next.js + FastAPI + DB + Auth + Payments)",
    "web-app": "Web app standalone (Next.js + Vercel Functions)",
    "ai-agent": "Agente AI autônomo (Python + Agno/LangChain)",
    "cli-tool": "Ferramenta CLI distribuível (Python + Typer)",
}


def list_templates() -> None:
    print("\nTemplates disponíveis:\n")
    for name, description in AVAILABLE_TEMPLATES.items():
        print(f"  {name:<12} {description}")
    print()


def scaffold(template: str, name: str, output: Path) -> None:
    src = TEMPLATES_DIR / template
    if not src.exists():
        print(f"Erro: template '{template}' não encontrado.")
        print(f"Templates disponíveis: {', '.join(AVAILABLE_TEMPLATES)}")
        sys.exit(1)

    dest = output / name
    if dest.exists():
        print(f"Erro: diretório '{dest}' já existe.")
        sys.exit(1)

    print(f"\nCriando projeto '{name}' a partir do template '{template}'...")
    shutil.copytree(src, dest)

    # Substituir placeholder "mycli" / nome genérico pelo nome do projeto
    _replace_in_tree(dest, "mycli", name.lower().replace("-", "_"))
    _replace_in_tree(dest, "TEMPLATE_NAME", name)
    _replace_in_tree(dest, "TEMPLATE_DATE", datetime.now().strftime("%Y-%m-%d"))

    print(f"✓ Projeto criado em: {dest}")
    print(f"\nPróximos passos:")
    print(f"  cd {dest}")
    print(f"  cat README.md")


def _replace_in_tree(root: Path, old: str, new: str) -> None:
    for path in root.rglob("*"):
        if path.is_file() and not _is_binary(path):
            try:
                content = path.read_text(encoding="utf-8")
                if old in content:
                    path.write_text(content.replace(old, new), encoding="utf-8")
            except (UnicodeDecodeError, PermissionError):
                pass


def _is_binary(path: Path) -> bool:
    binary_extensions = {".png", ".jpg", ".jpeg", ".gif", ".ico", ".woff", ".woff2", ".ttf"}
    return path.suffix.lower() in binary_extensions


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Vibecoder Scaffold — cria projetos a partir de templates"
    )
    parser.add_argument("--template", "-t", help="Nome do template")
    parser.add_argument("--name", "-n", help="Nome do novo projeto")
    parser.add_argument(
        "--output", "-o", type=Path, default=Path.cwd(), help="Diretório de saída (default: .)"
    )
    parser.add_argument("--list", "-l", action="store_true", help="Listar templates disponíveis")

    args = parser.parse_args()

    if args.list:
        list_templates()
        return

    if not args.template or not args.name:
        parser.print_help()
        print("\nExemplo: python scaffold.py --template saas --name meu-produto")
        sys.exit(1)

    scaffold(args.template, args.name, args.output)


if __name__ == "__main__":
    main()

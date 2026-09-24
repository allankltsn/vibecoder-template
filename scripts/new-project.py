#!/usr/bin/env python3
"""new-project.py — Cria um novo projeto satélite a partir de um template do hub."""

import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

HUB_DIR = Path(__file__).parent.parent
TEMPLATES_DIR = HUB_DIR / "templates"

AVAILABLE_TEMPLATES = {
    "saas": "Produto SaaS completo (Next.js + FastAPI + Auth + Billing)",
    "web-app": "Web app Next.js standalone com Vercel Functions",
    "ai-agent": "Agente AI autônomo (Python + Agno/LangChain + Tools)",
    "cli-tool": "Ferramenta CLI distribuível (Python + Typer + Rich)",
}


def list_templates() -> None:
    print("\nTemplates disponíveis:\n")
    for name, desc in AVAILABLE_TEMPLATES.items():
        print(f"  {name:<12} {desc}")
    print("\nUso: python scripts/new-project.py <template> <nome> [diretório]")
    print("     python scripts/new-project.py saas meu-produto ~/projetos/\n")


def create_project(template: str, name: str, output_dir: Path) -> None:
    src = TEMPLATES_DIR / template
    if not src.exists():
        print(f"[erro] Template '{template}' não encontrado.")
        list_templates()
        sys.exit(1)

    slug = name.lower().replace(" ", "-")
    dest = output_dir / slug
    if dest.exists():
        print(f"[erro] Diretório '{dest}' já existe.")
        sys.exit(1)

    print(f"\nCriando projeto '{slug}' a partir do template '{template}'...")
    shutil.copytree(src, dest, ignore=shutil.ignore_patterns("*.pyc", "__pycache__", ".venv"))

    replacements = {
        "mycli": slug.replace("-", "_"),
        "TEMPLATE_NAME": name,
        "TEMPLATE_SLUG": slug,
        "TEMPLATE_DATE": datetime.now().strftime("%Y-%m-%d"),
    }
    _replace_in_tree(dest, replacements)

    # Criar .vibecoder.json — rastreia a origem do projeto
    manifest = {
        "hub": str(HUB_DIR),
        "template": template,
        "name": name,
        "slug": slug,
        "created_at": datetime.now().isoformat(),
        "hub_version": _get_hub_version(),
    }
    (dest / ".vibecoder.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(f"\n✓ Projeto criado em: {dest.resolve()}")
    print("\nPróximos passos:")
    print(f"  cd {dest.resolve()}")
    print("  cat README.md")
    print(f"  claude .   # abre Claude Code no projeto")


def _replace_in_tree(root: Path, replacements: dict[str, str]) -> None:
    binary_ext = {".png", ".jpg", ".jpeg", ".gif", ".ico", ".woff", ".woff2", ".ttf", ".bin"}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix in binary_ext:
            continue
        try:
            content = path.read_text(encoding="utf-8")
            for old, new in replacements.items():
                content = content.replace(old, new)
            path.write_text(content, encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            pass


def _get_hub_version() -> str:
    version_file = HUB_DIR / "VERSION"
    return version_file.read_text().strip() if version_file.exists() else "unknown"


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="new-project",
        description="Vibecoder Hub — criar novo projeto satélite",
    )
    parser.add_argument("template", nargs="?", help="Tipo de template")
    parser.add_argument("name", nargs="?", help="Nome do projeto")
    parser.add_argument("output", nargs="?", type=Path, default=Path.cwd(), help="Diretório de saída")
    parser.add_argument("--list", "-l", action="store_true", help="Listar templates")

    args = parser.parse_args()

    if args.list or not args.template:
        list_templates()
        return

    if not args.name:
        print("[erro] Informe o nome do projeto.")
        print(f"Uso: python scripts/new-project.py {args.template} <nome>")
        sys.exit(1)

    create_project(args.template, args.name, args.output)


if __name__ == "__main__":
    main()

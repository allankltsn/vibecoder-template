#!/usr/bin/env python3
"""status.py — Overview de projetos satélite criados a partir deste hub."""

import json
import subprocess
from pathlib import Path
from datetime import datetime

HUB_DIR = Path(__file__).parent.parent


def find_satellites(search_dirs: list[Path]) -> list[dict]:
    """Encontra projetos satélite que têm .vibecoder.json."""
    satellites = []
    for search_dir in search_dirs:
        if not search_dir.exists():
            continue
        for manifest_path in search_dir.glob("*/.vibecoder.json"):
            try:
                data = json.loads(manifest_path.read_text(encoding="utf-8"))
                data["path"] = str(manifest_path.parent)
                data["_git_status"] = _get_git_status(manifest_path.parent)
                satellites.append(data)
            except (json.JSONDecodeError, KeyError):
                pass
    return sorted(satellites, key=lambda x: x.get("created_at", ""), reverse=True)


def _get_git_status(project_dir: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "status", "--short"],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=5,
        )
        lines = [l for l in result.stdout.strip().splitlines() if l]
        if not lines:
            return "limpo"
        return f"{len(lines)} arquivo(s) modificado(s)"
    except (subprocess.SubprocessError, FileNotFoundError):
        return "sem git"


def print_status(satellites: list[dict]) -> None:
    if not satellites:
        print("\nNenhum projeto satélite encontrado.")
        print("\nCrie um com: python scripts/new-project.py saas meu-projeto")
        return

    print(f"\n{'=' * 60}")
    print(f"  Vibecoder Hub — {len(satellites)} projeto(s) satélite")
    print(f"{'=' * 60}")

    for s in satellites:
        created = s.get("created_at", "")[:10]
        template = s.get("template", "?")
        name = s.get("name", "?")
        path = s.get("path", "?")
        git = s.get("_git_status", "?")

        print(f"\n  {name}")
        print(f"    Template : {template}")
        print(f"    Criado   : {created}")
        print(f"    Git      : {git}")
        print(f"    Caminho  : {path}")

    print(f"\n{'=' * 60}\n")


def main() -> None:
    # Procura em diretórios comuns de projetos
    home = Path.home()
    search_dirs = [
        home / "projetos",
        home / "projects",
        home / "dev",
        home / "code",
        Path("C:/projetos") if Path("C:/").exists() else None,
    ]
    search_dirs = [d for d in search_dirs if d is not None]

    satellites = find_satellites(search_dirs)
    print_status(satellites)

    if not satellites:
        print("Dica: projetos são detectados pelo arquivo '.vibecoder.json'")
        print("gerado automaticamente pelo script new-project.py")


if __name__ == "__main__":
    main()

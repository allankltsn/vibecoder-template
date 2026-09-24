#!/usr/bin/env python3
"""sync-hub.py — Sincroniza configs do hub para um projeto satélite.

Atualiza: AGENTS.md, orca/, subagentes .claude/agents/
Preserva: CLAUDE.md local (específico do projeto), código do projeto
"""

import argparse
import shutil
import sys
from pathlib import Path

HUB_DIR = Path(__file__).parent.parent

SYNC_TARGETS = {
    "AGENTS.md": "AGENTS.md",
    "orca/orca.yaml": "orca/orca.yaml",
    "orca/profiles": "orca/profiles",
}

OPTIONAL_AGENTS = [
    "architect.md",
    "fullstack-dev.md",
    "ai-engineer.md",
    "qa-engineer.md",
    "deployer.md",
    "content-writer.md",
]


def sync(project_dir: Path, dry_run: bool = False) -> None:
    if not project_dir.exists():
        print(f"[erro] Diretório '{project_dir}' não encontrado.")
        sys.exit(1)

    print(f"\nSincronizando hub → {project_dir.resolve()}")
    if dry_run:
        print("(modo dry-run: mostrará o que seria feito, sem modificar nada)\n")

    changes = 0

    # Sincronizar arquivos mapeados
    for src_rel, dest_rel in SYNC_TARGETS.items():
        src = HUB_DIR / src_rel
        dest = project_dir / dest_rel

        if not src.exists():
            continue

        if src.is_file():
            if not dry_run:
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dest)
            print(f"  ✓ {dest_rel}")
            changes += 1
        elif src.is_dir():
            if not dry_run:
                if dest.exists():
                    shutil.rmtree(dest)
                shutil.copytree(src, dest)
            print(f"  ✓ {dest_rel}/ (diretório)")
            changes += 1

    # Sincronizar subagentes (apenas os que já existem no projeto)
    agents_src = HUB_DIR / ".claude" / "agents"
    agents_dest = project_dir / ".claude" / "agents"
    if agents_dest.exists():
        for agent_file in OPTIONAL_AGENTS:
            src = agents_src / agent_file
            dest = agents_dest / agent_file
            if src.exists():
                if not dry_run:
                    shutil.copy2(src, dest)
                print(f"  ✓ .claude/agents/{agent_file}")
                changes += 1

    if changes == 0:
        print("  Nada para sincronizar.")
    else:
        print(f"\n✓ {changes} arquivo(s) sincronizados.")
        if not dry_run:
            print("  CLAUDE.md local NÃO foi modificado (específico do projeto).")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="sync-hub",
        description="Sincroniza configs globais do hub para um projeto satélite",
    )
    parser.add_argument("project", type=Path, help="Caminho para o projeto satélite")
    parser.add_argument("--dry-run", action="store_true", help="Mostrar o que seria feito")

    args = parser.parse_args()
    sync(args.project, dry_run=args.dry_run)


if __name__ == "__main__":
    main()

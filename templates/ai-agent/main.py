#!/usr/bin/env python3
"""Entry point do agente AI."""

import os
from dotenv import load_dotenv

load_dotenv()

from agents.base import create_agent


def main() -> None:
    agent = create_agent()
    print("Agente iniciado. Digite 'sair' para encerrar.\n")

    while True:
        user_input = input("Você: ").strip()
        if user_input.lower() in ("sair", "exit", "quit"):
            break
        if not user_input:
            continue

        response = agent.run(user_input)
        print(f"\nAgente: {response}\n")


if __name__ == "__main__":
    main()

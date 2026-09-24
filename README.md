# Vibecoder Template — Option B: Templates Isolados

> Coleção de templates de projeto prontos para uso. Cada template é independente,
> com suas próprias configs de Claude Code, Codex e Orca.

## Templates disponíveis

| Template | Quando usar | Stack |
|----------|------------|-------|
| [saas/](templates/saas/) | Produto SaaS completo com auth, billing | Next.js + FastAPI + DB |
| [web-app/](templates/web-app/) | Web app simples sem backend próprio | Next.js + Vercel Functions |
| [ai-agent/](templates/ai-agent/) | Agente AI autônomo ou assistente | Python + LangChain/Agno |
| [cli-tool/](templates/cli-tool/) | Ferramenta CLI distribuível | Python + Click/Typer |

## Criar novo projeto a partir de um template

```bash
# Instalação única do scaffold
pip install -e scripts/

# Criar novo projeto SaaS
python scripts/scaffold.py --template saas --name meu-produto --output ~/projetos/

# Criar agente AI
python scripts/scaffold.py --template ai-agent --name meu-agente --output ~/projetos/

# Ver todos os templates
python scripts/scaffold.py --list
```

## Quando usar esta opção

✅ Projetos variados com stacks diferentes  
✅ Quer copiar um template limpo sem bagagem do monorepo  
✅ Times diferentes usando templates diferentes  
⚠️ Não há compartilhamento de código entre projetos (duplique o que precisar)  
⚠️ Manter configs de agentes em sync requer disciplina  

## Como funciona cada template

Cada template tem:
- `README.md` — instruções específicas do template
- `.claude/CLAUDE.md` — instruções Claude Code para o tipo de projeto
- `AGENTS.md` — instruções para Codex e outros agentes
- `orca.yaml` — perfis Orca específicos para o tipo de projeto
- Código inicial funcional (não só esqueleto)

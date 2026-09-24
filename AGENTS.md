# Vibecoder Hub — Global Agent Instructions

> Este arquivo é injetado pelo Orca em todos os agentes que trabalham neste hub
> e nos projetos satélite que o referenciam.

## Contexto do projeto

Este é o **Vibecoder Hub** — repositório central de templates, configs de agentes
e scripts de automação para um dev full-stack Python + TypeScript.

Stack padrão dos projetos satélite:
- **Frontend**: Next.js 15, TypeScript, Tailwind CSS, shadcn/ui
- **Backend**: FastAPI, Python 3.12+, uv, Pydantic v2
- **Deploy**: Vercel (web) + Railway (api/db quando necessário)
- **AI**: Claude (anthropic), OpenAI, Agno, LangChain

## Princípios universais

1. **YAGNI**: implemente apenas o que o usuário pediu
2. **Types primeiro**: TypeScript strict, Python com type hints completo
3. **Server-side por padrão**: dados no servidor, não no cliente
4. **Sem secrets no código**: sempre via variáveis de ambiente
5. **Testes que importam**: cubra comportamento, não implementação

## Padrão de resposta

Quando implementar algo:
1. Verifique se existe código similar para reusar
2. Siga os padrões existentes do projeto
3. Implemente com tipos explícitos
4. Adicione testes para comportamentos críticos
5. Documente apenas o WHY não-óbvio (não o WHAT)

## Commit message

```
tipo(escopo): descrição curta em minúsculas

Tipos: feat | fix | refactor | test | docs | chore
```

## Nunca faça
- Commitar `.env` ou qualquer arquivo com secrets
- Usar `any` em TypeScript sem justificativa
- Criar abstrações antes de ter 3 casos de uso
- Escrever comentários que descrevem O QUE o código faz

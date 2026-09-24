# Workflow Completo — Do Branding ao Deploy

Guia prático de como cada fase do desenvolvimento usa o Hub.

---

## Fase 1: Branding e Conceito

**Ferramentas**: Claude Code + agent `content-writer`  
**Output**: identidade visual, copy, nome do produto

```bash
# No hub
claude .

# Invoke content-writer para nome e tagline
> Use content-writer: crie um nome e tagline para um SaaS de X
```

**Checklist de branding:**
- [ ] Nome (único, domínio disponível, .com.br ou .io)
- [ ] Tagline (1 frase, benefício concreto)
- [ ] Cores primárias (1 principal + 1 accent)
- [ ] Font (1 para headings + 1 para corpo)
- [ ] Logo (Figma/Penpot — arquivos SVG)

**Onde salvar:** `~/projetos/<nome>/apps/web/src/styles/brand.ts`

---

## Fase 2: Criar o Projeto

```bash
# Criar novo projeto satélite
python scripts/new-project.py saas meu-produto ~/projetos/

# Entrar no projeto
cd ~/projetos/meu-produto

# Abrir Claude Code
claude .
```

---

## Fase 3: Desenvolvimento (Loop)

### A: Claude Code (interativo, 1 agente)
Para trabalho focado no contexto atual do projeto:

```bash
claude .
> implemente a página de login com Clerk
> use architect: projete o schema do banco para multi-tenancy
> use qa-engineer: escreva testes para o endpoint de pagamento
```

### B: Codex (rápido, sem contexto de projeto)
Para tasks isoladas, boilerplate, refactoring:

```bash
codex "add TypeScript types for the User model in src/types/user.ts"
```

### C: Orca (paralelo, múltiplos agentes)
Para features importantes onde você quer mais de uma perspectiva:

```bash
# Da raiz do projeto (precisa do orca.yaml)
orca run --profile feature --task "implement user settings page with name, email, and avatar upload"

# Orca roda Claude + Codex em paralelo
# Você vê os 2 diffs e escolhe o melhor (ou combina)
orca apply  # aplica a solução escolhida
```

---

## Fase 4: Qualidade

```bash
# Type check + lint
pnpm check
uv run ruff check .

# Testes
pnpm test
uv run pytest -v

# Review via Orca
orca run --profile review --task "review PR changes in src/app/(app)/settings/"
```

---

## Fase 5: Deploy

### Vercel (automático)
```bash
# Setup inicial (uma vez)
vercel link
vercel env add ANTHROPIC_API_KEY production
vercel env add DATABASE_URL production

# Deploy
git push origin main  # Vercel detecta e deploya automaticamente
```

### Preview antes de mergear
```bash
vercel  # cria preview URL para o PR
```

---

## Quando usar qual agente

| Situação | Agente/Ferramenta |
|---------|-------------------|
| Decidir arquitetura | `architect` via Claude Code |
| Feature frontend + backend | `fullstack-dev` ou Orca `feature` |
| Feature LLM/AI | `ai-engineer` via Claude Code |
| Bug crítico | Orca `bugfix` |
| Code review | Orca `review` |
| Landing page copy | `content-writer` via Claude Code |
| Boilerplate rápido | Codex direto |
| Deploy/CI | `deployer` via Claude Code |

---

## Fluxo semanal sugerido

```
Segunda:   Planejamento — defina as 3 features da semana
Terça-Qui: Desenvolvimento — use o loop da Fase 3
Sexta:     QA + Review — Orca review + ajustes + deploy
```

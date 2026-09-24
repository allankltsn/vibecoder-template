# Do Branding ao Deploy — Guia Passo a Passo

Checklist completo para lançar um produto do zero usando o Vibecoder Hub.

---

## 0. Setup do Hub (uma vez)

```bash
git clone https://github.com/allankltsn/vibecoder-template.git ~/vibecoder-hub
cd ~/vibecoder-hub
```

---

## 1. Branding (Dia 1)

- [ ] Definir nome do produto (checar domínio em namecheap.com ou registro.br)
- [ ] Criar tagline (1 frase, benefício concreto, para quem)
- [ ] Escolher paleta de cores (shadcn/ui theme customizado)
- [ ] Escolher tipografia (Google Fonts — 1 heading + 1 body)
- [ ] Criar logo (Penpot — open source, grátis)
- [ ] Exportar assets: `logo.svg`, `favicon.ico`, `og-image.png` (1200x630)

**Ferramenta**: `use content-writer: crie nome e tagline para [descrição do produto]`

---

## 2. Setup do Projeto (Dia 1-2)

```bash
# Criar projeto satélite
python ~/vibecoder-hub/scripts/new-project.py saas <nome> ~/projetos/

cd ~/projetos/<nome>

# Configurar ambiente
cp .env.example .env.local
# Preencher: ANTHROPIC_API_KEY, CLERK_*, DATABASE_URL, STRIPE_*

# Instalar dependências
pnpm install
uv sync

# Testar setup
pnpm dev
```

---

## 3. Landing Page (Dia 2-4)

Estrutura mínima viável:

```
Hero           → Headline + Subheadline + CTA + (screenshot ou demo)
Como funciona  → 3 passos simples
Benefícios     → 3-4 cards com ícones
Pricing        → 2-3 planos com toggle mensal/anual
FAQ            → 5-8 perguntas reais de usuários
CTA final      → Repita o CTA principal
```

**Ferramenta**: `use content-writer: escreva a seção hero da landing page para [produto]`

---

## 4. Auth e Onboarding (Dia 3-5)

- [ ] Configurar Clerk (criar app em clerk.com, adicionar keys)
- [ ] Implementar `apps/web/src/middleware.ts` (proteger rotas `/dashboard/*`)
- [ ] Criar fluxo de onboarding (collect basic user info pós-signup)
- [ ] Testar login com Google + email/password

---

## 5. Core Feature (Semana 2)

```bash
# Usar Orca para features importantes
orca run --config ~/vibecoder-hub/orca/orca.yaml \
  --profile feature \
  --task "implement [core feature description]"
```

- [ ] Feature principal implementada e testada
- [ ] Endpoint FastAPI com testes
- [ ] UI funcional no dashboard
- [ ] Error states tratados (loading, empty, error)

---

## 6. Pagamentos (Semana 2-3)

- [ ] Criar conta Stripe e adicionar keys
- [ ] Implementar `apps/api/src/services/billing.py`
- [ ] Criar produtos e preços no Stripe Dashboard
- [ ] Configurar webhook (`/api/v1/webhooks/stripe`)
- [ ] Testar com cartão de teste Stripe

**Stripe test card**: `4242 4242 4242 4242`, exp: qualquer data futura, CVC: qualquer

---

## 7. QA e Launch Prep (Semana 3)

```bash
# Code review completo
orca run --profile review --task "review all changes since initial commit"

# Testes
pnpm test && uv run pytest -v

# Build check
pnpm build
```

- [ ] Todos os fluxos críticos testados manualmente
- [ ] Lighthouse score > 90 (Performance, Accessibility, SEO)
- [ ] Meta tags e OG tags corretas
- [ ] Política de privacidade e termos de uso
- [ ] Analytics configurado (Vercel Analytics ou Plausible)

---

## 8. Deploy (Semana 3-4)

```bash
# Conectar ao Vercel
vercel link

# Configurar variáveis de produção
vercel env add ANTHROPIC_API_KEY production
vercel env add CLERK_SECRET_KEY production
vercel env add DATABASE_URL production
vercel env add STRIPE_SECRET_KEY production

# Deploy produção
vercel --prod

# Configurar domínio customizado
vercel domains add meu-produto.com.br
```

- [ ] Domínio configurado e SSL ativo
- [ ] Stripe webhook apontando para produção
- [ ] Testar fluxo completo em produção
- [ ] Configurar alertas (Vercel Alerts ou Better Uptime)

---

## 9. Lançamento

- [ ] Anunciar no LinkedIn, Twitter/X, Product Hunt
- [ ] Enviar para early users / lista de espera
- [ ] Monitorar erros nas primeiras 48h (Vercel Logs)
- [ ] Iterar com base no feedback

---

## Ferramentas recomendadas (gratuitas/open-source)

| Categoria | Ferramenta | Por quê |
|-----------|-----------|---------|
| Design | Penpot | Open source, alternativa ao Figma |
| Analytics | Plausible | Privacy-first, leve |
| Monitoramento | Better Uptime | Uptime + alertas de email |
| Email | Resend | API simples, 3k emails/mês grátis |
| DB | Neon | PostgreSQL serverless, free tier generoso |
| Deploy | Vercel | Zero config para Next.js |
| Pagamentos | Stripe | Padrão de mercado |

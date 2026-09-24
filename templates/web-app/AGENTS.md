# Web App — Agent Instructions

Next.js 15 standalone + Vercel Functions.

## Mapa
| Localização | Responsabilidade |
|-------------|-----------------|
| src/app/(marketing)/ | Páginas públicas |
| src/app/(app)/ | Páginas autenticadas |
| src/app/api/ | Vercel Functions (REST) |
| src/components/features/ | Componentes de domínio |
| src/lib/ | Utilitários e clientes API |

## Regras
1. Server Components por padrão
2. `"use client"` somente para interatividade real
3. Env vars privadas nunca no frontend
4. Images via `next/image` com `sizes`

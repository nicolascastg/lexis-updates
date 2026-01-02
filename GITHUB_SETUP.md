# Configuração do Repositório GitHub para Lexis

## Estrutura do Repositório

O repositório `lexis-updates` deve ter a seguinte estrutura:

```
lexis-updates/
├── version.json              # Versão do instalador (app principal)
├── users.enc                 # Lista de usuários autorizados
├── README.md
└── modules/                  # Módulos atualizáveis
    ├── version.json          # Versão dos módulos
    ├── prompts.py            # System prompts (atualizável)
    ├── ai_config.json        # Configurações de IA
    └── legal_triggers.json   # Triggers de busca jurídica
```

## Como Funciona

### 1. Atualização do APP (Instalador)
- App verifica `/version.json` na raiz do repositório
- Se há nova versão → baixa instalador e reinstala
- Usado para mudanças grandes (UI, core, novos recursos)

### 2. Atualização de MÓDULOS (Sem reinstalar)
- App verifica `/modules/version.json`
- Se há módulos novos → baixa apenas os arquivos alterados
- Substitui localmente → pede reinício simples
- Usado para: prompts, configurações, triggers de busca

## Fluxo de Atualização

```
[App Inicia]
    │
    ├── Verifica version.json (app)
    │   └── Nova versão? → Diálogo: "Nova versão disponível"
    │
    └── Verifica modules/version.json
        └── Módulos novos? → Diálogo: "Atualizações disponíveis"
                              └── Atualizar → Baixa arquivos → Reinicia
```

## Como Atualizar Módulos

### Para atualizar prompts:
1. Edite `modules/prompts.py` no repositório
2. Atualize a versão em `modules/version.json`:
   ```json
   {
     "version": "1.1.0",
     "modules": {
       "prompts.py": "1.1.0",
       ...
     }
   }
   ```
3. Commit e push
4. Usuários receberão notificação na próxima abertura do app

### Para atualizar configurações de IA:
1. Edite `modules/ai_config.json`
2. Atualize versão correspondente
3. Commit e push

## Vantagens

✅ Atualizações rápidas sem reinstalação
✅ Prompts podem ser ajustados em tempo real
✅ Configurações de IA flexíveis
✅ Triggers de busca atualizáveis
✅ Rollback fácil (versão anterior fica como .bak)

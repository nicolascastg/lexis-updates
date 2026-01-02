# 🚀 Guia de Deploy - Lexis v2.8.0

## Parte 1: Configurando o GitHub

### 1.1. Estrutura do Repositório

O repositório `lexis-updates` deve ter esta estrutura:

```
lexis-updates/
├── version.json              ← Controla versão do INSTALADOR
├── users.enc                 ← Usuários autorizados
├── README.md
├── GITHUB_SETUP.md
├── DEPLOY_GUIDE.md
└── modules/                  ← MÓDULOS ATUALIZÁVEIS
    ├── version.json          ← Controla versão dos MÓDULOS
    ├── prompts.py
    ├── ai_config.json
    └── legal_triggers.json
```

### 1.2. Passo a Passo

```bash
# 1. Clone ou acesse o repositório
cd C:\Users\tdcad\Documents\GitHub\lexis-updates

# 2. Extraia github_repo_v2.8.0.zip na raiz
# Isso vai criar/atualizar:
#   - version.json
#   - modules/
#   - GITHUB_SETUP.md
#   - etc.

# 3. Commit e push
git add .
git commit -m "v2.8.0 - Sistema de módulos atualizáveis"
git push origin main
```

### 1.3. Criar Release no GitHub

1. Vá para: https://github.com/nicolascastg/lexis-updates/releases
2. Clique em **"Draft a new release"**
3. Preencha:
   - **Tag:** `v2.8.0`
   - **Title:** `Lexis v2.8.0 - Módulos Atualizáveis`
   - **Description:**
     ```
     ## Novidades
     - 🔄 Sistema de módulos atualizáveis (sem reinstalar!)
     - ✅ Correção do "Fale mais" nos pop-ups
     - 📅 Data dinâmica correta nos prompts
     - ⚡ Prompts otimizados
     
     ## Atualização
     Baixe e execute o instalador abaixo.
     ```
4. Anexe o arquivo: `Lexis_Setup_v2.8.0.exe`
5. Clique em **"Publish release"**

---

## Parte 2: Build do Instalador

### 2.1. No seu computador de desenvolvimento

```powershell
# 1. Extrair o código
cd C:\Users\tdcad\Downloads
# Extraia lexis_v2.8.0_FINAL.zip para pasta "lexis"

# 2. Entrar na pasta
cd lexis

# 3. Limpar builds anteriores
rd /s /q build dist

# 4. Gerar executável
pyinstaller installer/lexis.spec

# 5. Verificar resultado
dir dist\Lexis\
# Deve ter Lexis.exe e várias DLLs
```

### 2.2. Compilar Instalador (Inno Setup)

1. Abra o **Inno Setup Compiler**
2. Abra o arquivo: `installer\lexis_setup.iss`
3. Pressione **Ctrl+F9** para compilar
4. O instalador será criado em: `dist\Lexis_Setup_v2.8.0.exe`

---

## Parte 3: Instalando nos Computadores dos Usuários

### 3.1. Primeira Instalação (Novo Usuário)

1. **Baixe o instalador** da página de releases do GitHub
2. **Execute** `Lexis_Setup_v2.8.0.exe`
3. **Siga o assistente** de instalação
4. O instalador vai:
   - Instalar o Lexis em `C:\Program Files\Lexis`
   - Instalar Ollama (se não tiver)
   - Baixar modelo de IA (llama3.2)
   - Criar atalhos

### 3.2. Atualização (Usuário Existente)

#### Opção A: Atualização Automática (Recomendado)
1. Ao abrir o Lexis, ele detecta automaticamente nova versão
2. Clique em **"Baixar Atualização"**
3. Execute o instalador baixado
4. Pronto!

#### Opção B: Atualização Manual
1. Baixe o instalador da página de releases
2. Execute o instalador (ele fecha o Lexis automaticamente)
3. Siga o assistente
4. Pronto!

### 3.3. Atualização de Módulos (Sem Reinstalar!)

A partir da v2.8.0, algumas atualizações não precisam de reinstalação:

1. Ao abrir o Lexis, ele verifica módulos automaticamente
2. Se há atualizações, aparece diálogo: **"Atualizações Disponíveis"**
3. Clique em **"Atualizar Agora"**
4. App baixa apenas os arquivos alterados
5. Reinicia automaticamente
6. **Pronto! Sem reinstalar!**

---

## Parte 4: Atualizando Módulos no Futuro

### 4.1. Para atualizar PROMPTS:

```bash
# 1. Edite o arquivo no GitHub
# modules/prompts.py

# 2. Atualize a versão
# modules/version.json
{
  "version": "1.1.0",  # Incrementar
  "modules": {
    "prompts.py": "1.1.0"  # Incrementar
  }
}

# 3. Commit e push
git add modules/
git commit -m "Prompts atualizados"
git push
```

**Resultado:** Todos os usuários receberão notificação na próxima abertura!

### 4.2. Para atualizar CONFIGURAÇÕES de IA:

```bash
# Edite modules/ai_config.json
# Atualize versão em modules/version.json
# Commit e push
```

### 4.3. Para atualizar TRIGGERS de BUSCA:

```bash
# Edite modules/legal_triggers.json
# Atualize versão em modules/version.json
# Commit e push
```

---

## Parte 5: Verificação

### 5.1. Testar se está funcionando

1. **No GitHub**, verifique:
   - https://raw.githubusercontent.com/nicolascastg/lexis-updates/main/version.json
   - https://raw.githubusercontent.com/nicolascastg/lexis-updates/main/modules/version.json

2. **No Lexis**, verifique:
   - Abra o app
   - Veja no console se aparece `[ModuleUpdater]`
   - Ou espere aparecer diálogo de atualização

### 5.2. Logs úteis

O Lexis mostra logs no console (se executado pelo código):
```
[Lexis] Verificando módulos...
[ModuleUpdater] Módulos para atualizar: ['prompts.py']
[ModuleUpdater] ✓ prompts.py atualizado
```

---

## Resumo Rápido

| O que atualizar | Onde editar | Precisa reinstalar? |
|-----------------|-------------|---------------------|
| UI, Core, Recursos novos | Código + Instalador | ✅ Sim |
| Prompts | `modules/prompts.py` | ❌ Não |
| Config de IA | `modules/ai_config.json` | ❌ Não |
| Triggers de busca | `modules/legal_triggers.json` | ❌ Não |
| Usuários autorizados | `users.enc` | ❌ Não (atualiza no login) |


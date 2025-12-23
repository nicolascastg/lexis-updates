# Lexis - Sistema de Atualizações

Este repositório contém os arquivos de atualização do Lexis - Assistente Jurídico Inteligente.

## 📁 Estrutura

```
lexis-updates/
├── version.json    # Informações da versão atual
└── README.md       # Este arquivo
```

## 🔄 Como Funciona

1. O Lexis verifica `version.json` ao iniciar
2. Se houver versão mais nova, mostra notificação ao usuário
3. Usuário clica para baixar o instalador do GitHub Releases
4. Executa o instalador e atualiza

## 📋 Como Lançar uma Nova Versão

### Passo 1: Gere o novo instalador
```bash
# No projeto Lexis
pyinstaller installer/lexis.spec
# Compile com Inno Setup
```

### Passo 2: Crie uma Release no GitHub
1. Vá em **Releases** > **Create new release**
2. Tag: `v2.7.0` (exemplo)
3. Título: `Lexis v2.7.0`
4. Anexe o arquivo `Lexis_Setup_v2.7.0.exe`
5. Publique

### Passo 3: Atualize version.json
```json
{
    "version": "2.7.0",
    "download_url": "https://github.com/nicolascastg/lexis-updates/releases/download/v2.7.0/Lexis_Setup_v2.7.0.exe",
    "release_notes": "- Correção X\n- Melhoria Y\n- Nova funcionalidade Z",
    "mandatory": false
}
```

### Passo 4: Commit e Push
```bash
git add version.json
git commit -m "Atualização v2.7.0"
git push
```

## 📝 Campos do version.json

| Campo | Descrição |
|-------|-----------|
| `version` | Versão atual (ex: "2.7.0") |
| `download_url` | Link direto para o instalador |
| `release_notes` | Notas da versão (use \n para quebras de linha) |
| `mandatory` | Se `true`, força atualização (não implementado ainda) |

## ⚠️ Importante

- Mantenha este repositório **privado** se o instalador contiver API keys
- Ou use repositório **público** e peça a API key na primeira execução

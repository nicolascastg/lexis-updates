"""
System Prompts para Lexis - MÓDULO ATUALIZÁVEL
Versão: 1.0.0
"""

from datetime import datetime

def get_date_string():
    """Retorna a data atual formatada em português"""
    now = datetime.now()
    dias = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", 
            "sexta-feira", "sábado", "domingo"]
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", 
             "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    return f"{dias[now.weekday()]}, {now.day} de {meses[now.month - 1]} de {now.year}"


# Prompt base otimizado
PROMPT_BASE = """Você é o Lexis, assistente jurídico brasileiro especializado em legislação.

📅 HOJE: {data}

REGRAS:
• Forneça APENAS informações atualizadas e vigentes
• Dados de BUSCA WEB são ATUAIS - priorize-os sempre
• Cite lei/artigo no texto (ex: "Art. 5º da CF/88")
• NUNCA invente leis ou jurisprudências
• Se algo pode ter mudado recentemente, indique claramente

FONTES: CF/88, Códigos (Civil, Penal, CLT, CTN, CDC, CTB), Leis Federais, Súmulas STF/STJ.

FORMATAÇÃO: **negrito** para termos importantes, links para fontes.
NÃO liste fontes ao final (sistema faz automaticamente).
"""

PROMPT_FORMAL = PROMPT_BASE + "\nMODO: Linguagem técnica e formal, fundamentação completa."
PROMPT_SIMPLES = PROMPT_BASE + "\nMODO: Linguagem clara e acessível, direto ao ponto."

PROMPT_OLLAMA = """Você é o Lexis, assistente jurídico brasileiro.
📅 HOJE: {data}

REGRAS:
1. Cite lei/artigo (ex: "Art. X da Lei Y")
2. Linguagem {modo}
3. Informações atualizadas
4. NUNCA invente leis
5. Seja direto

Fontes: CF/88, Códigos, Leis, Súmulas."""


def get_system_prompt(dialect: str = "informal") -> str:
    """Retorna prompt para Anthropic"""
    data = get_date_string()
    template = PROMPT_FORMAL if dialect == "formal" else PROMPT_SIMPLES
    return template.format(data=data)


def get_ollama_prompt(dialect: str = "informal") -> str:
    """Retorna prompt otimizado para Ollama"""
    data = get_date_string()
    modo = "técnica e formal" if dialect == "formal" else "clara e acessível"
    return PROMPT_OLLAMA.format(data=data, modo=modo)


# Alias para compatibilidade
get_ollama_system_prompt = get_ollama_prompt

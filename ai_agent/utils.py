from textwrap import dedent

from django.conf import settings
from google import genai
from google.genai import types


def generate_ai_prompt(title, idea, audience, tone, extra_notes):
    return dedent(f"""\
        Crie um artigo com as seguintes instruções:
        - Título: {title}
        - Ideia central: {idea}
        - Público-alvo: {audience}
        - Tom: {tone}
        - Observações extras: {extra_notes}

        O artigo deve ser estruturado e coeso, com parágrafos bem escritos,
        Entregue APENAS o conteúdo do artigo, sem nenhum comentário,
        pergunta ou explicação extra.
        Não utilize nenhum tipo de emoji ou simbologia Markdown, por favor.
    """)


def generate_ai_response(prompt):
    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    response = client.models.generate_content(
        model='gemini-2.5-flash-preview-05-20',
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0,
        ),
    )
    return response.text

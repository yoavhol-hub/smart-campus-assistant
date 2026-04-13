import logging

from openai import OpenAI
from app.config import settings

logger = logging.getLogger(__name__)

client = OpenAI(api_key=settings.openai_api_key)


def generate_ai_answer(question: str, category: str, context: str) -> str:
    system_prompt = f"""
You are Smart Campus Assistant, a helpful university campus assistant.

Rules:
- Answer only using the campus context
- Do not invent information
- If unsure, say you are not confident
- Keep answers short and clear
- Category: {category}

Context:
{context}
""".strip()

    response = client.responses.create(
        model=settings.openai_model,
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
    )

    answer = response.output_text.strip()
    logger.info("AI answer generated successfully for category '%s'", category)
    return answer
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

print("OPENAI_API_KEY loaded:", bool(api_key))
print("OPENAI_MODEL loaded:", model)

client = OpenAI(api_key=api_key)


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
        model=model,
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
    )

    return response.output_text.strip()
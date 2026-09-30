from gemini_client import generate_text

SYSTEM = """You are EduGenie, a friendly educational assistant.
Answer academic questions accurately and clearly.
Use simple language appropriate for the requested learner level.
Do not invent citations or claim you verified information externally.
If the question is ambiguous, state the assumption briefly.
Prefer a concise answer followed by a short example when useful."""


async def answer_question(question: str, level: str) -> str:
    prompt = f"""
Learner level: {level}

Question:
{question}

Give a clear educational answer. Use headings or bullets only when they improve
readability. Keep the response focused on the question.
"""
    return generate_text(prompt, system_instruction=SYSTEM, max_output_tokens=1000)

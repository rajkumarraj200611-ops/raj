from gemini_client import generate_text


async def summarize_text(text: str, level: str) -> str:
    prompt = f"""
Summarize the following educational text for a {level}-level learner.

Requirements:
- Preserve the main facts and meaning.
- Remove repetition and minor details.
- Use simple language.
- End with 3-5 key points.

Text:
{text}
"""
    return generate_text(
        prompt,
        system_instruction="You are EduGenie's concise educational summarizer.",
        temperature=0.25,
        max_output_tokens=1200,
    )

from config import settings
from gemini_client import generate_text


async def _gemini_explanation(topic: str, level: str) -> str:
    prompt = f"""
Explain the topic "{topic}" to a {level}-level learner.

Structure the explanation as:
1. Simple definition
2. How it works
3. One easy real-world/example use case
4. Key points to remember

Avoid unnecessary jargon. If a technical term is required, define it simply.
"""
    return generate_text(
        prompt,
        system_instruction="You are EduGenie's concept-explanation tutor.",
        temperature=0.35,
        max_output_tokens=1000,
    )


def _local_explanation(topic: str, level: str) -> str:
    # Loaded only when explicitly enabled so the normal installation remains light.
    from transformers import pipeline

    generator = pipeline(
        "text2text-generation",
        model=settings.local_model,
    )
    prompt = (
        f"Explain {topic} simply for a {level} student. "
        "Give a definition, how it works, an example, and key points."
    )
    result = generator(prompt, max_new_tokens=300, do_sample=False)
    return result[0]["generated_text"]


async def explain_topic(topic: str, level: str) -> str:
    if settings.local_explanation_enabled:
        try:
            return _local_explanation(topic, level)
        except Exception:
            # Cloud fallback keeps the application usable if the local model
            # is unavailable or cannot be loaded.
            pass
    return await _gemini_explanation(topic, level)

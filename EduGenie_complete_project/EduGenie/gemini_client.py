from functools import lru_cache

from google import genai
from google.genai import types

from config import settings


class GeminiNotConfiguredError(RuntimeError):
    pass


@lru_cache(maxsize=1)
def get_client() -> genai.Client:
    if not settings.gemini_api_key:
        raise GeminiNotConfiguredError(
            "GEMINI_API_KEY is missing. Add it to the .env file."
        )
    return genai.Client(api_key=settings.gemini_api_key)


def generate_text(
    prompt: str,
    *,
    system_instruction: str | None = None,
    temperature: float = 0.4,
    max_output_tokens: int = 1200,
    response_mime_type: str | None = None,
    response_schema=None,
) -> str:
    config_kwargs = {
        "temperature": temperature,
        "max_output_tokens": max_output_tokens,
    }

    if system_instruction:
        config_kwargs["system_instruction"] = system_instruction

    if response_mime_type:
        config_kwargs["response_mime_type"] = response_mime_type

    if response_schema is not None:
        config_kwargs["response_schema"] = response_schema

    response = get_client().models.generate_content(
        model=settings.gemini_model,
        contents=prompt,
        config=types.GenerateContentConfig(**config_kwargs),
    )

    text = getattr(response, "text", None)
    if not text:
        raise RuntimeError("Gemini returned an empty response.")
    return text.strip()

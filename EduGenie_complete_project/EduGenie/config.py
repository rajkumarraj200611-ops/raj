import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    local_explanation_enabled: bool = (
        os.getenv("LOCAL_EXPLANATION_ENABLED", "false").lower() == "true"
    )
    local_model: str = os.getenv(
        "LOCAL_MODEL", "MBZUAI/LaMini-Flan-T5-783M"
    )


settings = Settings()

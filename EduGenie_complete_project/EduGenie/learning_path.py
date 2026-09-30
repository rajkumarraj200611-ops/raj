import json

from gemini_client import generate_text
from schemas import LearningPathResponse


async def get_learning_recommendations(
    topic: str, level: str, hours_per_week: float
) -> dict:
    prompt = f"""
Create a personalized learning path for: {topic}

Current learner level: {level}
Available study time: {hours_per_week} hours per week

Include beginner-to-advanced progression where appropriate.
Provide practical study steps, estimated time, resources to look for
(videos/articles/books can be described by type or title), and practice tasks.
Do not invent URLs.

Return exactly 4 to 6 steps.
"""
    raw = generate_text(
        prompt,
        system_instruction="You are EduGenie's structured learning-path planner.",
        temperature=0.35,
        max_output_tokens=2200,
        response_mime_type="application/json",
        response_schema=LearningPathResponse,
    )
    return LearningPathResponse.model_validate(json.loads(raw)).model_dump()

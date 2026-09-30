import json

from gemini_client import generate_text
from schemas import QuizResponse


async def generate_quiz(text: str, level: str) -> dict:
    prompt = f"""
Create exactly 3 multiple-choice questions from the educational passage below.

Learner level: {level}

Passage:
{text}

Rules:
- Exactly 3 questions.
- Exactly 4 options per question.
- correct_answer must be exactly one of the four option strings.
- Include a short explanation for the correct answer.
- Questions must be answerable from the passage or basic reasoning about it.
"""
    raw = generate_text(
        prompt,
        system_instruction="You create fair educational quizzes.",
        temperature=0.25,
        max_output_tokens=1600,
        response_mime_type="application/json",
        response_schema=QuizResponse,
    )
    return QuizResponse.model_validate(json.loads(raw)).model_dump()

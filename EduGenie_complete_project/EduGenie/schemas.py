from pydantic import BaseModel, Field


class QARequest(BaseModel):
    question: str = Field(min_length=1, max_length=8000)
    level: str = Field(default="beginner", max_length=50)


class ExplainRequest(BaseModel):
    topic: str = Field(min_length=1, max_length=4000)
    level: str = Field(default="beginner", max_length=50)


class QuizRequest(BaseModel):
    text: str = Field(min_length=1, max_length=12000)
    level: str = Field(default="beginner", max_length=50)


class SummaryRequest(BaseModel):
    text: str = Field(min_length=1, max_length=20000)
    level: str = Field(default="beginner", max_length=50)


class LearningPathRequest(BaseModel):
    topic: str = Field(min_length=1, max_length=2000)
    level: str = Field(default="beginner", max_length=50)
    hours_per_week: float = Field(default=5, ge=1, le=40)


class QuizQuestion(BaseModel):
    question: str
    options: list[str] = Field(min_length=4, max_length=4)
    correct_answer: str
    explanation: str


class QuizResponse(BaseModel):
    questions: list[QuizQuestion] = Field(min_length=3, max_length=3)


class LearningStep(BaseModel):
    stage: str
    topics: list[str]
    suggested_time: str
    resources: list[str]
    practice: list[str]


class LearningPathResponse(BaseModel):
    topic: str
    learner_level: str
    overview: str
    steps: list[LearningStep]

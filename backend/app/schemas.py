from pydantic import BaseModel, Field, field_validator


class AskRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        max_length=500,
        description="User campus-related question",
        examples=["Where is the main library?"],
    )

    @field_validator("question")
    @classmethod
    def validate_question(cls, value: str) -> str:
        cleaned = value.strip()

        if not cleaned:
            raise ValueError("Question cannot be empty.")

        if len(cleaned) < 3:
            raise ValueError("Question must be at least 3 characters long.")

        return cleaned


class AskResponse(BaseModel):
    question: str
    category: str
    answer: str
    used_fallback: bool
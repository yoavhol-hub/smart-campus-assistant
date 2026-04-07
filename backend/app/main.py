from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.schemas import AskRequest, AskResponse
from app.services.classifier import classify_question
from app.services.fallback import should_fallback, fallback_message
from app.services.answer_service import get_relevant_context
from app.services.ai_service import generate_ai_answer
from app.data.db import SessionLocal
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Smart Campus Assistant API is running"}


@app.post("/ask", response_model=AskResponse)
def ask_question(payload: AskRequest, db: Session = Depends(get_db)):
    category = classify_question(payload.question)

    if should_fallback(payload.question):
        return AskResponse(
            question=payload.question,
            category=category,
            answer=fallback_message(category),
            used_fallback=True
        )

    context = get_relevant_context(
    payload.question,
    category if category != "unknown" else None,
    db
)

    if not context:
        return AskResponse(
            question=payload.question,
            category=category,
            answer="I could not find relevant campus information for this question.",
            used_fallback=True
        )

    try:
        ai_answer = generate_ai_answer(
            question=payload.question,
            category=category,
            context=context
        )
    except Exception as e:
        print("AI ERROR:", repr(e))
        return AskResponse(
        question=payload.question,
        category=category,
        answer="The AI service is currently unavailable. Please try again later.",
        used_fallback=True
    )
    

    if not ai_answer:
        return AskResponse(
            question=payload.question,
            category=category,
            answer="I could not generate a reliable answer.",
            used_fallback=True
        )

    return AskResponse(
        question=payload.question,
        category=category,
        answer=ai_answer,
        used_fallback=False
    )
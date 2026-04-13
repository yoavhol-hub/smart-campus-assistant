import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import AskRequest, AskResponse
from app.services.classifier import classify_question
from app.services.fallback import should_fallback, fallback_message
from app.services.answer_service import get_relevant_context
from app.services.ai_service import generate_ai_answer
from app.data.db import SessionLocal

logger = logging.getLogger(__name__)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def read_root():
    return {"message": "Smart Campus Assistant API is running"}


@router.post("/ask", response_model=AskResponse)
def ask_question(payload: AskRequest, db: Session = Depends(get_db)):
    logger.info("Received question: %s", payload.question)

    category = classify_question(payload.question)
    logger.info("Predicted category: %s", category)

    if should_fallback(payload.question):
        logger.warning("Fallback triggered for question: %s", payload.question)
        return AskResponse(
            question=payload.question,
            category=category,
            answer=fallback_message(category),
            used_fallback=True,
        )

    context = get_relevant_context(
        payload.question,
        category if category != "unknown" else None,
        db,
    )

    if not context:
        logger.info("No relevant context found for question: %s", payload.question)
        return AskResponse(
            question=payload.question,
            category=category,
            answer="I could not find relevant campus information for this question.",
            used_fallback=True,
        )

    try:
        ai_answer = generate_ai_answer(
            question=payload.question,
            category=category,
            context=context,
        )
    except Exception:
        logger.exception("AI service failed while generating an answer")
        return AskResponse(
            question=payload.question,
            category=category,
            answer="The AI service is currently unavailable. Please try again later.",
            used_fallback=True,
        )

    if not ai_answer or not ai_answer.strip():
        logger.warning("AI returned an empty answer")
        return AskResponse(
            question=payload.question,
            category=category,
            answer="I could not generate a reliable answer.",
            used_fallback=True,
        )

    logger.info("Answer generated successfully")
    return AskResponse(
        question=payload.question,
        category=category,
        answer=ai_answer,
        used_fallback=False,
    )
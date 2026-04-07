from app.data.db import SessionLocal
from app.data.seed import seed_data
from app.services.answer_service import get_relevant_context


def test_get_relevant_context_returns_medical_clinic():
    seed_data()

    db = SessionLocal()
    try:
        question = "Where is the medical clinic?"
        context = get_relevant_context(question, None, db)

        assert context != ""
        assert "medical clinic" in context.lower()
    finally:
        db.close()
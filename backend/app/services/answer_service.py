import re
from sqlalchemy.orm import Session
from app.data.models import CampusInfo


STOP_WORDS = {
    "the", "is", "a", "an", "of", "to", "in", "on", "at",
    "for", "and", "or", "how", "do", "i", "my", "can",
    "there", "what", "when", "where", "are", "me", "please"
}


def normalize_text(text: str) -> list[str]:
    cleaned_text = re.sub(r"[^a-zA-Z0-9\s]", "", text.lower())
    words = cleaned_text.split()
    return [word for word in words if word not in STOP_WORDS]


def calculate_score(question_words: set[str], topic_words: set[str], content_words: set[str]) -> int:
    topic_overlap = question_words & topic_words
    content_overlap = question_words & content_words

    score = (len(topic_overlap) * 3) + (len(content_overlap) * 1)

    if topic_words and topic_words.issubset(question_words):
        score += 5

    return score


def get_relevant_context(question: str, category: str | None, db: Session) -> str:
    query = db.query(CampusInfo)

    # אם יש קטגוריה → חפש בה
    if category and category != "unknown":
        query = query.filter(CampusInfo.category == category)

    records = query.all()

    if not records:
        return ""

    question_words = set(normalize_text(question))
    scored_records = []

    for record in records:
        topic_words = set(normalize_text(record.topic.replace("_", " ")))
        content_words = set(normalize_text(record.content))

        score = calculate_score(question_words, topic_words, content_words)
        scored_records.append((score, record))

    # מיין לפי score
    scored_records.sort(key=lambda item: item[0], reverse=True)

    # קח רק התאמות אמיתיות
    top_records = [record for score, record in scored_records if score > 0][:3]

    # 🔥 תיקון חשוב — אם לא נמצא כלום בקטגוריה → ננסה הכל
    if not top_records and category:
        return get_relevant_context(question, None, db)

    if not top_records:
        return ""

    context_parts = []
    for record in top_records:
        context_parts.append(
            f"Topic: {record.topic}\n"
            f"Content: {record.content}\n"
            f"Source: {record.source}"
        )

    return "\n\n".join(context_parts)
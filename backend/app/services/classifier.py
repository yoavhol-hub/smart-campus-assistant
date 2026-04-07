def classify_question(question: str) -> str:
    q = question.lower()

    schedule_keywords = [
        "exam", "schedule", "when", "hours", "open", "deadline", "class", "date", "time"
    ]

    general_keywords = [
        "where", "room", "building", "office", "location", "library", "parking"
    ]

    technical_keywords = [
        "wifi", "wi-fi", "internet", "portal", "password", "login", "technical", "error"
    ]

    if any(word in q for word in schedule_keywords):
        return "schedule"

    if any(word in q for word in general_keywords):
        return "general"

    if any(word in q for word in technical_keywords):
        return "technical"

    return "unknown"
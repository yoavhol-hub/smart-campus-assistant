def should_fallback(question: str) -> bool:
    """
    Return True only for clearly invalid input.
    Fallback should not depend on classification.
    """
    q = question.strip()

    if not q:
        return True

    return False


def fallback_message(category: str) -> str:
    """
    Return a user-friendly fallback message when no reliable answer was found.
    """
    if category == "unknown":
        return (
            "I could not find a reliable campus-related answer for that question. "
            "Please try asking about schedules, rooms, campus services, or technical support."
        )

    return (
        "I could not find a reliable answer based on the available campus information. "
        "Please rephrase your question or contact the relevant campus office."
    )
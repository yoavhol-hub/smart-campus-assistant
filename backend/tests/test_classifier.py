from app.services.classifier import classify_question


def test_classify_schedule_question():
    result = classify_question("When is my next class?")
    assert result == "schedule"


def test_classify_technical_question():
    result = classify_question("The campus Wi-Fi is not working")
    assert result == "technical"


def test_classify_general_question():
    result = classify_question("Where is the library?")
    assert result == "general"
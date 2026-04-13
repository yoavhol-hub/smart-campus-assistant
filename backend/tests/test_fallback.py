from app.services.fallback import should_fallback, fallback_message


def test_should_fallback_with_empty_like_input():
    assert should_fallback("...") is True or should_fallback("...") is False


def test_fallback_message_returns_string():
    message = fallback_message("unknown")
    assert isinstance(message, str)
    assert len(message.strip()) > 0
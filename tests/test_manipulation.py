from agents.manipulation_detector import detect_manipulation


def test_normal_text():

    result = detect_manipulation(
        "The government announced a new transport policy."
    )

    assert result["risk"] == "LOW"


def test_clickbait():

    result = detect_manipulation(
        "BREAKING!!! Share this now! Government hiding the truth!"
    )

    assert result["risk"] == "HIGH"


def test_secret_cure():

    result = detect_manipulation(
        "Doctors don't want you to know this secret cure."
    )

    assert result["score"] >= 20

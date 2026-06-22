def detect_deepfake(content):

    suspicious = [
        "viral video",
        "leaked footage",
        "exclusive clip",
        "deepfake",
        "ai generated",
        "shocking video",
        "watch this video",
        "hidden camera footage"
    ]

    text = content.lower()

    matches = 0

    for word in suspicious:
        if word in text:
            matches += 1

    if matches >= 3:
        return {
            "deepfake_risk": "High",
            "confidence": 90
        }

    elif matches >= 1:
        return {
            "deepfake_risk": "Medium",
            "confidence": 70
        }

    else:
        return {
            "deepfake_risk": "Not Applicable",
            "confidence": 50
        }
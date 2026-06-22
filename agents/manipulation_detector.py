import json
import os
import re

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "manipulation_rules.json"
)

with open(file_path, "r") as f:
    RULES = json.load(f)


def detect_manipulation(text):

    score = 0
    signals = []

    text_lower = text.lower()

    # Fear language
    if any(word in text_lower for word in RULES["fear_words"]):
        score += 20
        signals.append("Fear Language")

    # Share request
    if any(word in text_lower for word in RULES["share_words"]):
        score += 20
        signals.append("Share Request")

    # Clickbait
    if any(word in text_lower for word in RULES["clickbait_words"]):
        score += 20
        signals.append("Clickbait")

    # Excessive exclamation
    if text.count("!") >= 3:
        score += 20
        signals.append("Sensational Language")

    # ALL CAPS detection
    words = text.split()

    caps_words = [
        word for word in words
        if len(word) > 3 and word.isupper()
    ]

    if len(caps_words) >= 2:
        score += 20
        signals.append("ALL CAPS")

    score = min(score, 100)

    if score <= 30:
        risk = "LOW"
    elif score <= 70:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    return {
        "score": score,
        "signals": signals,
        "risk": risk
    }
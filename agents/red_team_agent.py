def red_team_review(claim):

    suspicious_words = [
        "always",
        "never",
        "guaranteed",
        "100%",
        "miracle",
        "secret"
    ]

    claim_lower = claim.lower()

    for word in suspicious_words:
        if word in claim_lower:
            return {
                "challenge_found": True,
                "confidence": 40,
                "reason": f"Suspicious term detected: {word}"
            }

    return {
        "challenge_found": False,
        "confidence": 90,
        "reason": "No obvious manipulation indicators found."
    }

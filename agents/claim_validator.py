def validate_claim(claim):

    vague_words = [
    "government",
    "they",
    "everyone",
    "always",
    "never",
    "truth",
    "secret",
    "secretly",
    "guaranteed",
    "coverup",
    "hidden",
    "breaking"
   ]

    score = 100
    issues = []

    if len(claim.split()) < 5:
        score -= 20
        issues.append("Claim too short")

    for word in vague_words:
        if word.lower() in claim.lower():
            score -= 10
            issues.append(f"Contains vague term: {word}")

    return {
        "validity_score": max(score, 0),
        "issues": issues
    }
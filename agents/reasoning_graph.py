def generate_reasoning(result):

    steps = []

    if result.get("extracted_claim"):
        steps.append("Claim Extracted")

    if result.get("evidence"):
        steps.append("Evidence Collected")

    if result.get("source_verification"):
        steps.append("Source Verified")

    if result.get("source_score"):
        steps.append("Credibility Assessed")

    if result.get("manipulation"):
        steps.append("Manipulation Checked")

    if result.get("red_team"):
        steps.append("Red Team Review")

    if result.get("deepfake"):
        steps.append("Deepfake Analysis")

    if result.get("risk_level"):
        steps.append("Risk Assessed")

    if result.get("verdict"):
        steps.append("Verdict Generated")

    return steps
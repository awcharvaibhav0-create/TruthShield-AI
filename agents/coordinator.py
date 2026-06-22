from fact_checker import fact_check
from source_verifier import verify_source
from risk_assessor import assess_risk
from verdict_agent import final_verdict
from claim_extractor import extract_claim
from evidence_search import search_evidence
from source_credibility import source_credibility
from red_team_agent import red_team_review
from manipulation_detector import detect_manipulation
from reasoning_graph import generate_reasoning
from deepfake_detector import detect_deepfake
from claim_validator import validate_claim



def analyze_claim(claim, source):

    claim_text = extract_claim(claim)
    validation = validate_claim(claim_text)
    validation_score = validation["validity_score"]
    if validation_score < 60:
        score -= 10
    manipulation_result = detect_manipulation(claim_text)
    manipulation_score = manipulation_result.get("score", 50)
    evidence = search_evidence(claim_text)

    support_count = len(evidence.get("supporting", []))
    contradict_count = len(evidence.get("contradicting", []))
    red_team_result = red_team_review(claim_text)
    credibility_score = source_credibility(source)
    fact_result = fact_check(claim_text)
    source_result = verify_source(source)
    deepfake_result = detect_deepfake(claim)
    print("DEBUG DEEPFAKE:", deepfake_result)
    risk_level = deepfake_result.get(
    "deepfake_risk",
    "low"
    ).lower()

    if risk_level == "high":
        deepfake_score = 10

    elif risk_level == "medium":
        deepfake_score = 50

    else:
        deepfake_score = 90

    if isinstance(source_result, dict):
        source_score = source_result.get("score", 50)
    else:
        source_score = 50
    fact_result_lower = fact_result.lower()
    if (
    "context" in fact_result_lower
    or "too broad" in fact_result_lower
    or "cannot verify" in fact_result_lower
    ):
        fact_score = 50

    elif "likely true" in fact_result_lower:
        fact_score = 90

    elif "true" in fact_result_lower:
        fact_score = 85

    elif "false" in fact_result_lower:
        fact_score = 20

    elif "uncertain" in fact_result_lower:
        fact_score = 50

    else:
        fact_score = 60

    red_team_score = (
    100 -
    red_team_result.get("confidence", 50)
    )

    

    score = int(
    fact_score * 0.25 +
    credibility_score * 0.15 +
    source_score * 0.15 +
    red_team_score * 0.05 +
    deepfake_score * 0.05+
    validation_score * 0.20 +
    (100 - manipulation_score) * 0.25


    )

    
    evidence_bonus = (support_count - contradict_count) * 5

    score += evidence_bonus

    score = max(0, min(score, 100))
    bonus = 0
    if source:
        trusted_domains = [
        "who.int",
        "reuters.com",
        "apnews.com",
        "bbc.com",
        "nature.com"
       ]

    

        for domain in trusted_domains:
            if domain in source.lower():
                bonus = 10
                break

    score += bonus
    score = min(score, 100)

    
    risk = assess_risk(manipulation_score)
    print("Trusted Source Bonus:", bonus)
    if manipulation_score >= 80:
        verdict = "🚨 Potentially Manipulative"

    elif score >= 85:
        verdict = "✅ Likely True"

    elif score >= 70:
        verdict = "⚠️ Needs Verification"

    elif score >= 50:
        verdict = "❓ Uncertain"

    else:
        verdict = "❌ Likely False"
    reasoning = generate_reasoning({
    "extracted_claim": claim_text,
    "evidence": evidence,
    "source_verification": source_result,
    "manipulation": manipulation_result,
    "red_team": red_team_result,
    "deepfake": deepfake_result,
    "risk_level": risk,
    "verdict": verdict
})
    print("Fact Score:", fact_score)
    print("Manipulation Score:", manipulation_score)
    print("Source Score:", source_score)
    print("Credibility Score:", credibility_score)
    print("Red Team Score:", red_team_score)
    print("Deepfake Score:", deepfake_score)
    print("Final Truth Score:", score)
    print("Verdict:", verdict)

    return {
    "extracted_claim": claim_text,
    "fact_check": fact_result,
    "fact_score": fact_score,
    "evidence": evidence,
    "source_verification": source_result,
    "credibility_score": credibility_score,
    "source_score": source_score,
    "red_team": red_team_result,
    "truth_score": score,
    "risk_level": risk,
    "verdict": verdict,
    "manipulation": manipulation_result,
    "manipulation_score": manipulation_score,
    "reasoning": reasoning,
    "deepfake": deepfake_result,
    "claim_validation": validation,
    "trusted_bonus": bonus,
    "support_count": support_count,
    "contradict_count": contradict_count,
    "evidence_bonus": evidence_bonus
}
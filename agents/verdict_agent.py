def final_verdict(score):

    if score >= 80:
        return "✅ Likely True"

    elif score >= 60:
        return "⚠️ Needs Verification"

    elif score >= 40:
        return "❓ Uncertain"

    else:
        return "❌ Likely False"
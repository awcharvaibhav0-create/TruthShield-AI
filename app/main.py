import streamlit as st
import sys
import os
import plotly.graph_objects as go
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "agents")
    )
)

from coordinator import analyze_claim

st.title("TruthShield AI")
st.subheader("Misinformation Detection Platform")

claim = st.text_area("Enter a claim")
source = st.text_input("Source")
if st.button("Analyze"):
    st.session_state["result"] = analyze_claim(claim, source)

if "result" in st.session_state:
    result = st.session_state["result"]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Truth Score",
            f"{result['truth_score']}%"
        )

    with col2:
        st.metric(
            "Fact Score",
            result["fact_score"]
        )
    fig = go.Figure(
        go.Indicator(
        mode="gauge+number",
        value=result["truth_score"],
        title={"text": "Trust Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "green"},
            "steps": [
                {"range": [0, 40], "color": "red"},
                {"range": [40, 70], "color": "orange"},
                {"range": [70, 100], "color": "green"}
            ]
        }
    )
)

    st.plotly_chart(fig)
    st.progress(result["truth_score"] / 100)
    st.write("### Extracted Claim")
    st.info(result["extracted_claim"])
    st.write("### Claim Validation")

    validation = result["claim_validation"]

    st.metric(
        "Validity Score",
        validation["validity_score"]
    )

    for issue in validation["issues"]:
        st.warning(issue)

    st.write("### Fact Check")
    st.write(result["fact_check"])

    evidence = result.get("evidence", {})

    st.write("### Supporting Evidence")

    if evidence.get("supporting"):
        for item in evidence["supporting"]:

            if isinstance(item, dict):
                st.markdown(
                    f"✅ [{item['title']}]({item['url']})"
            )
            else:
                st.success(item)

    else:
      st.info("No supporting evidence found.")

    st.write("### Contradicting Evidence")

    if evidence.get("contradicting"):
        for item in evidence["contradicting"]:

            if isinstance(item, dict):
                st.markdown(
                    f"⚠️ [{item['title']}]({item['url']})"
                    )
            else:
                st.warning(item)

    else:
        st.info("No contradicting evidence found.")

    st.write("### Evidence Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Supporting Sources",
             result["support_count"]
        )

    with col2:
        st.metric(
            "Contradicting Sources",
            result["contradict_count"]
        )

    with col3:
        st.metric(
            "Evidence Bonus",
            result["evidence_bonus"]
       )

    st.write("### Manipulation Analysis")

    man = result["manipulation"]
    fig2 = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=man["score"],
        title={"text": "Manipulation Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "steps": [
                {"range": [0, 30], "color": "green"},
                {"range": [30, 70], "color": "orange"},
                {"range": [70, 100], "color": "red"}
            ]
        }
    )
)

    st.plotly_chart(fig2)

    st.metric(
    "Manipulation Score",
    man["score"]
)

    st.progress(
    man["score"] / 100
)

    if man["risk"] == "HIGH":
        st.error("🚨 HIGH RISK")

    elif man["risk"] == "MEDIUM":
        st.warning("⚠️ MEDIUM RISK")

    else:
        st.success("✅ LOW RISK")

    st.write("### Detected Signals")

    if man["signals"]:
        for signal in man["signals"]:
            st.warning(signal)
    else:
        st.success("No manipulation indicators found.")


    st.write("### Source Verification")
    verification = result["source_verification"]

    if isinstance(verification, dict):
        st.success(
            f"Source: {verification['source']} "
            f"(Score: {verification['score']})"
        )
    else:
        st.write(verification)
    st.write("### Source Credibility")

    st.metric(
    "Credibility Score",
    result["source_score"]
)

    st.progress(
    result["source_score"] / 100
)

    score = result["source_score"]

    if score >= 90:
        st.success("Highly Trusted Source")

    elif score >= 70:
        st.info("Moderately Trusted Source")

    else:
        st.warning("Low Credibility Source")

    st.write("### Red Team Analysis")

    if result["red_team"]["challenge_found"]:
        st.warning(result["red_team"]["reason"])
    else:
        st.success(result["red_team"]["reason"])

    st.write("### Risk Level")

    if result["risk_level"] == "High Risk":
        st.error("🚨 High Risk")

    elif result["risk_level"] == "Medium Risk":
        st.warning("⚠️ Medium Risk")

    else:
        st.success("✅ Low Risk")
    st.write("DEBUG VERDICT:", result["verdict"])
    st.write("### Final Verdict")

    verdict = result["verdict"]

    if "Likely True" in verdict:
        st.success(verdict)

    elif "Needs Verification" in verdict:
        st.warning(verdict)

    else:
        st.error(verdict)

    st.write("### Reasoning Flow")

    for i, step in enumerate(result["reasoning"], 1):
        st.markdown(f"**{i}.** {step}")

    st.write("### Deepfake Detection")

    deepfake = result["deepfake"]

    risk = deepfake.get("deepfake_risk", "Unknown")
    confidence = deepfake.get("confidence", 0)

    if risk == "Low":
        st.success(
            f"✅ Deepfake Risk: {risk} | Confidence: {confidence}%"
       )

    elif risk == "Medium":
        st.warning(
            f"⚠️ Deepfake Risk: {risk} | Confidence: {confidence}%"
        )

    else:
        st.error(
            f"🚨 Deepfake Risk: {risk} | Confidence: {confidence}%"
        )
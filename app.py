import streamlit as st
import pandas as pd

# 🔗 Import all modules
from chatbot import get_response
from precautions import get_precautions
from risk_reason import get_risk_reason
from severity import get_severity_score
from attacks import possible_attacks
from report import generate_report

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="🛡️ Cybersecurity Risk Detector",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #e0f7fa, #ffffff);
}
section.main > div {
    background-color: #ffffff;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}
h1, h2, h3 {
    font-family: 'Segoe UI', sans-serif;
    color: #0f4c75;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("""
<h1 style='text-align:center;'>🛡️ Cybersecurity Risk Detector</h1>
<p style='text-align:center;'>Analyze your system security risk (Offline AI System)</p>
<hr>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("🧾 Instructions")
    st.write("""
    1. Enter system details  
    2. Click Predict  
    3. View risk, attacks & precautions  
    """)
    st.info("This project works fully offline without APIs.")

# ---------------- INPUT FORM ----------------
with st.form("cyber_form"):
    st.subheader("🛠️ Enter System Details")

    vulnerabilities = st.number_input("Number of Vulnerabilities", 0, 100, 5)
    uptime = st.number_input("System Uptime (days)", 0, 1000, 30)
    incidents = st.number_input("Security Incidents", 0, 50, 1)
    patch = st.selectbox("Patch Frequency", ["Daily", "Weekly", "Monthly"])
    ports = st.slider("Open Ports", 0, 100, 10)

    submitted = st.form_submit_button("🔍 Predict Risk")

# ---------------- RISK LOGIC ----------------
def predict_risk(vuln, uptime, incidents, patch, ports):
    score = (vuln * 2) + (incidents * 3) + ports
    if patch == "Monthly":
        score += 10
    elif patch == "Weekly":
        score += 5

    if score < 20:
        return "Low Risk"
    elif score < 40:
        return "Medium Risk"
    else:
        return "High Risk"

# ---------------- OUTPUT ----------------
if submitted:
    st.subheader("📊 Input Summary")
    df = pd.DataFrame([{
        "Vulnerabilities": vulnerabilities,
        "Uptime": uptime,
        "Incidents": incidents,
        "Patch": patch,
        "Open Ports": ports
    }])
    st.dataframe(df, use_container_width=True)

    # 🔮 Predict
    risk = predict_risk(vulnerabilities, uptime, incidents, patch, ports)

    st.subheader("🚦 Predicted Risk Level")
    st.success(risk)

    # 🧠 Risk Explanation
    st.subheader("🧠 Risk Explanation")
    st.info(get_risk_reason(risk))

    # 📊 Severity
    st.subheader("📊 Severity Level")
    st.progress(get_severity_score(risk))

    # ⚠️ Possible Attacks
    st.subheader("⚠️ Possible Cyber Attacks")
    for attack in possible_attacks(risk):
        st.write("•", attack)

    # 🛡️ Auto Precautions
    st.subheader("🛡️ Recommended Security Precautions")
    for p in get_precautions(risk):
        st.warning(p)

    # 📄 Download Report
    st.subheader("📄 Security Report")
    st.download_button(
        label="⬇️ Download Security Report",
        data=generate_report(risk),
        file_name="cybersecurity_risk_report.txt"
    )

# ---------------- CHATBOT ----------------
st.markdown("---")
st.subheader("🤖 Cybersecurity Assistant (Offline Chatbot)")

user_query = st.text_input("Ask about risks, attacks, precautions, project...")

if user_query:
    st.info(get_response(user_query))

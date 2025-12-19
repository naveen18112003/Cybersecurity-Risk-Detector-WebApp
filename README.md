🛡️ Cybersecurity Risk Detector Web App (ML-Based)
📌 Project Overview

The Cybersecurity Risk Detector Web App is an ML-based and explainable cybersecurity assessment system built using Python and Streamlit.

The application uses a trained machine learning model to predict a system’s cybersecurity risk level (Low / Medium / High) and then provides:

Risk explanation (why this risk occurred)

Severity level

Possible cyber attacks

Auto-generated security precautions

Downloadable security report

Offline cybersecurity chatbot

👉 The entire system works offline and does not use any external APIs.

🎯 Problem Statement

Many systems are vulnerable to cyber attacks due to weak configurations, outdated software, and poor security practices.
Non-technical users often find it difficult to understand their system’s security risk.

This project simplifies cybersecurity assessment by converting basic system security indicators into meaningful ML-driven insights.

🚀 Key Features

🔮 Machine Learning-based Risk Prediction

🧠 Risk Explanation (Explainable AI)

📊 Severity Meter

⚠️ Possible Attack Prediction

🛡️ Auto Security Precautions

📄 Downloadable Cybersecurity Report

🤖 Offline Chatbot for Cyber Awareness

🔒 Fully Offline & Privacy-Friendly

🧠 Machine Learning Implementation

A dataset (veri.csv) was prepared using cybersecurity-related features.

Multiple ML algorithms were tested during experimentation.

The best-performing model was saved as a joblib file (eniyi.joblib).

The Streamlit app loads the trained model and performs real-time predictions using model.predict().

Model Type: Classification (Low / Medium / High Risk)

📂 Project Structure
Cybersecurity-Risk-Detector-WebApp/
│
├── app.py                 # Main Streamlit application
├── chatbot.py             # Offline chatbot logic
├── precautions.py         # Auto security precautions
├── risk_reason.py         # Risk explanation logic
├── severity.py            # Severity score calculation
├── attacks.py             # Possible cyber attacks
├── report.py              # Security report generation
├── veri.csv               # Dataset used for training
├── eniyi.joblib           # Trained ML model
├── veri.ipynb             # Model training notebook
├── README.md              # Documentation

🧮 Input Parameters & Where to Get Them (IMPORTANT)

The system requires five input parameters, which represent real-world cybersecurity indicators.

1️⃣ Number of Vulnerabilities

What it means:
Known security weaknesses in the system.

Where to get it from:

Vulnerability scanning tools (e.g., Nessus, OpenVAS)

Security audit reports

OS security assessments

Example: 5

2️⃣ System Uptime (in days)

What it means:
How long the system has been running without restart.

Where to get it from:

Windows: Task Manager → Performance → Uptime

Linux: uptime command

Example: 30

3️⃣ Number of Security Incidents

What it means:
Past security events such as malware detections, alerts, or failed login attempts.

Where to get it from:

Antivirus logs

Windows Event Viewer

Firewall logs

Example: 1

4️⃣ Patch Update Frequency

What it means:
How frequently security updates are applied.

Possible values:

Daily

Weekly

Monthly

Where to get it from:

OS update history

Organization patch management policies

5️⃣ Number of Open Ports

What it means:
Open network ports increase attack surface.

Where to get it from:

Windows: netstat -an

Linux: ss or nmap

Example: 10

🔍 Risk Prediction Workflow

User enters system security inputs

Inputs are converted into numerical features

Trained ML model predicts risk level

Explainable logic provides:

Risk reason

Severity score

Possible attacks

Auto precautions

Security report is generated

🛡️ Auto Security Precautions

Based on the predicted risk level, the system automatically recommends actions such as:

Password hardening

Firewall & antivirus activation

Data backup and encryption

Network access restrictions

📄 Cybersecurity Report

The user can download a detailed cybersecurity report containing:

Risk level

Severity score

Risk explanation

Possible attack types

Recommended precautions

🤖 Offline Chatbot

The built-in chatbot helps users:

Understand cybersecurity concepts

Ask about risks and attacks

Learn about security best practices

⚠️ The chatbot works offline and does not use any APIs.

▶️ How to Run the Project
pip install -r requirements.txt
streamlit run app.py

🎯 Conclusion

This project demonstrates how machine learning can be combined with explainable logic to build a practical, user-friendly cybersecurity risk assessment system suitable for real-world scenarios.

⭐ Author
Naveen Kumar Yadav
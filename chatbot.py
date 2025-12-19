def get_response(user_input):
    user_input = user_input.lower()

    responses = {

        "what is this project":
        "This project predicts cybersecurity risk using machine learning.",

        "how does it work":
        "User inputs are processed by an ML model to predict cyber risk level.",

        "low risk":
        "Low risk indicates basic security practices are followed.",

        "medium risk":
        "Medium risk indicates potential vulnerabilities.",

        "high risk":
        "High risk indicates serious security vulnerabilities.",

        "precaution":
        "Precautions are automatically generated based on risk level.",

        "phishing":
        "Phishing tricks users into revealing sensitive information.",

        "malware":
        "Malware is malicious software that damages systems.",

        "ransomware":
        "Ransomware encrypts data and demands payment.",

        "ddos":
        "DDoS attacks flood servers with traffic.",

        "future scope":
        "This project can be extended with real-time monitoring.",

        "limitations":
        "This system does not analyze real-time network traffic.",

        "help":
        "Ask about risk levels, attacks, precautions, or project details."
    }

    for key in responses:
        if key in user_input:
            return responses[key]

    return "Sorry, I didn't understand. Try asking about cybersecurity risks."

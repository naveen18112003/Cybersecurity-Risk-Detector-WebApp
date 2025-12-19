def possible_attacks(risk):

    if risk == "Low Risk":
        return ["Minor phishing attempts"]

    elif risk == "Medium Risk":
        return ["Phishing", "Malware", "Credential theft"]

    elif risk == "High Risk":
        return ["Ransomware", "Data breach", "DDoS", "Privilege escalation"]

    return []

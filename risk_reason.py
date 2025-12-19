def get_risk_reason(risk):

    if risk == "Low Risk":
        return "System follows most security best practices."

    elif risk == "Medium Risk":
        return "Some vulnerabilities like outdated software detected."

    elif risk == "High Risk":
        return "Critical vulnerabilities such as weak passwords or no firewall."

    return "Risk reason unavailable"

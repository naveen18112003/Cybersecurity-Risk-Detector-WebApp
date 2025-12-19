def get_severity_score(risk):
    scores = {
        "Low Risk": 20,
        "Medium Risk": 55,
        "High Risk": 90
    }
    return scores.get(risk, 0)

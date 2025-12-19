def get_precautions(risk):

    if risk == "Low Risk":
        return [
            "Keep system updated",
            "Use strong passwords",
            "Enable firewall",
            "Monitor system regularly"
        ]

    elif risk == "Medium Risk":
        return [
            "Enable 2FA",
            "Update all software",
            "Install antivirus",
            "Limit admin access"
        ]

    elif risk == "High Risk":
        return [
            "Change all passwords immediately",
            "Enable firewall & antivirus",
            "Perform security audit",
            "Backup and encrypt data",
            "Disconnect from public networks"
        ]

    return ["No precautions available"]

def get_risk_output(risk):
    if risk == "LOW":
        return "success", "Risk Level: LOW ✅"
    elif risk == "MEDIUM":
        return "warning", "Risk Level: MEDIUM ⚠"
    else:
        return "error", "Risk Level: HIGH 🚨"
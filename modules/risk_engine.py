def calculate_risk(symptoms):
    symptoms = symptoms.lower()

    score = 0

    if "chest pain" in symptoms:
        score += 5
    if "breathing" in symptoms:
        score += 4
    if "vomiting" in symptoms:
        score += 2
    if "blurred vision" in symptoms:
        score += 4
    if "fever" in symptoms:
        score += 1

    if score >= 8:
        return "HIGH RISK 🚨 Seek immediate medical care"
    elif score >= 4:
        return "MODERATE RISK ⚠ Monitor closely"
    else:
        return "LOW RISK ✅ Likely mild condition"

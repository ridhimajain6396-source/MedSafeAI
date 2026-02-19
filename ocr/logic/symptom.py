def get_symptom_advice(symptom):

    symptom = symptom.lower()

    if "fever" in symptom:
        return "Drink fluids, rest well, and monitor temperature."

    elif "cough" in symptom:
        return "Warm liquids and steam inhalation may help."

    elif "headache" in symptom:
        return "Rest in a quiet place and stay hydrated."

    else:
        return "Consult a doctor for proper diagnosis."
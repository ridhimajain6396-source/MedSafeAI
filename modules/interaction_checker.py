from modules.medicine_db import load_interactions

interactions = load_interactions()

def check_interactions(medicine_list):
    warnings = []
    for i in range(len(medicine_list)):
        for j in range(i+1, len(medicine_list)):
            a = medicine_list[i]["name"]
            b = medicine_list[j]["name"]

            for rule in interactions:
                if (rule["drug1"] == a and rule["drug2"] == b) or \
                   (rule["drug1"] == b and rule["drug2"] == a):
                    warnings.append(f"{a} + {b}: {rule['warning']}")
    return warnings

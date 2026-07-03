def classify_patient(ph_score, oxy_score, symptom_score):

    risk_score = ph_score + oxy_score + symptom_score

    if oxy_score == 3:
        return risk_score, "Critical (Severe Hypoxia)"

    if ph_score == 2 and symptom_score >= 1:
        return risk_score, "Critical (Severe Infection Risk)"

    if risk_score <= 2:
        return risk_score, "Healthy"

    elif risk_score <= 5:
        return risk_score, "Risk"

    else:
        return risk_score, "Critical"
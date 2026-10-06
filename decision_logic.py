def analyze_risk(predicted_risk, spo2, heart_rate, bp, temperature):

    score = 0

    # Scoring logic
    if bp > 140:
        score += 20
    if heart_rate > 100:
        score += 20
    if spo2 < 95:
        score += 25
    if temperature > 100:
        score += 15

    # Calculating Risk based on score
    if score >= 60:
        final_risk = "High"
    elif score >= 30:
        final_risk = "Medium"
    else:
        final_risk = "Low"

    # Emergency overrideing logic
    if spo2 < 90 or heart_rate > 120 or bp > 180:
        final_risk = "High"
        advice = "Emergency: Immediate medical attention required"
    elif final_risk == "Medium":
        advice = "Consult doctor and monitor condition"
    else:
        advice = "Low risk: Maintain healthy routine"

    return final_risk, score, advice
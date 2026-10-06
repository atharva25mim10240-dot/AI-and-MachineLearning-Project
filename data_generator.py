import csv
import random

# Number of data rows
num_rows = 2000

# Open CSV file
with open("dataset.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    # Header (column names)
    writer.writerow([
        "age", "gender", "bp", "heart_rate", "spo2",
        "bmi", "temperature", "smoker", "activity",
        "duration", "symptom_score", "risk"
    ])

    for _ in range(num_rows):

        # Generate random data
        age = random.randint(18, 80)
        gender = random.choice(["M", "F"])
        bp = random.randint(90, 180)
        heart_rate = random.randint(60, 120)
        spo2 = random.randint(85, 100)
        bmi = random.randint(18, 35)
        temperature = random.randint(97, 103)
        smoker = random.choice([0, 1])
        activity = random.choice(["low", "medium", "high"])
        duration = random.randint(1, 10)
        symptom_score = random.randint(1, 10)

        # Risk calculation logic (simulating AI decision logic)
        risk_score = 0

        if bp > 140:
            risk_score += 2
        if heart_rate > 100:
            risk_score += 2
        if spo2 < 92:
            risk_score += 3
        if temperature > 100:
            risk_score += 2
        if smoker == 1:
            risk_score += 1
        if symptom_score > 6:
            risk_score += 2

        # Final label
        if risk_score >= 7:
            risk = "High"
        elif risk_score >= 4:
            risk = "Moderate"
        else:
            risk = "Low"

        # Write row
        writer.writerow([
            age, gender, bp, heart_rate, spo2,
            bmi, temperature, smoker, activity,
            duration, symptom_score, risk
        ])

print("Dataset created successfully!")
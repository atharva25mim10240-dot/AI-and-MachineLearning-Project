import pickle
from decision_logic import analyze_risk

# Loading model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

def get_user_input():
    print("\n--- Enter Patient Details ---")

    age = int(input("Age: "))
    gender = input("Gender (M/F): ")
    bp = int(input("Blood Pressure: "))
    heart_rate = int(input("Heart Rate: "))
    spo2 = int(input("SpO2: "))
    bmi = int(input("BMI: "))
    temperature = int(input("Body Temperature: "))
    smoker = int(input("Smoker? (1 = Yes, 0 = No): "))
    activity = input("Activity (low/medium/high): ")
    duration = int(input("Duration (days): "))
    symptom_score = int(input("Symptom severity (1-10): "))

    # Converting categorical values
    gender = 0 if gender == "M" else 1

    if activity == "low":
        activity = 0
    elif activity == "medium":
        activity = 1
    else:
        activity = 2

    return [
        age, gender, bp, heart_rate, spo2,
        bmi, temperature, smoker, activity,
        duration, symptom_score
    ], spo2, heart_rate, bp, temperature


def run_system():
    data, spo2, heart_rate, bp, temperature = get_user_input()

    # ML Prediction
    prediction = model.predict([data])
    ml_result = prediction[0]

    # AI Logic
    final_risk, score, advice = analyze_risk(
        ml_result,
        spo2,
        heart_rate,
        bp,
        temperature
    )

    # Final Output
    print("\n--- RESULT ---")
    print("ML Prediction:", ml_result)
    print("Final Risk:", final_risk)
    print("Risk Score:", score)
    print("Advice:", advice)


# Runing program
run_system()
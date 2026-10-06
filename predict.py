from decision_logic import analyze_risk
import pickle

# Loading trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Taking input from user
age = int(input("Enter Age: "))
gender = input("Enter Gender (M/F): ")
bp = int(input("Enter Blood Pressure: "))
heart_rate = int(input("Enter Heart Rate: "))
spo2 = int(input("Enter SpO2: "))
bmi = int(input("Enter BMI: "))
temperature = int(input("Enter Body Temperature: "))
smoker = int(input("Smoker? (1 = Yes, 0 = No): "))
activity = input("Activity Level (low/medium/high): ")
duration = int(input("Duration of symptoms (days): "))
symptom_score = int(input("Symptom severity (1-10): "))

# Converting categorical values
if gender == "M":
    gender = 0
else:
    gender = 1

if activity == "low":
    activity = 0
elif activity == "medium":
    activity = 1
else:
    activity = 2

# Preparing input for model
input_data = [[
    age, gender, bp, heart_rate, spo2,
    bmi, temperature, smoker, activity,
    duration, symptom_score
]]

# ML Prediction
prediction = model.predict(input_data)
ml_result = prediction[0]

# AI Decision + Score
final_risk, score, advice = analyze_risk(
    ml_result,
    spo2,
    heart_rate,
    bp,
    temperature
)

# Output
print("\nML Predicted Risk:", ml_result)
print("Final Risk:", final_risk)
print("Risk Score (0-100):", score)
print("Advice:", advice)
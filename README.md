# AI-and-MachineLearning-Project

***

# Context-Aware Adaptive Patient Monitoring and Risk Escalation System

## Project Overview
This project is a **command-line based intelligent healthcare system** that analyzes patient health data and predicts the risk level using **Machine Learning** techniques.

In addition to prediction, the system also applies **rule-based logic** to identify critical conditions and provide appropriate medical recommendations. The goal of this project is to simulate a basic **decision-support system** that can assist in early health risk detection.

---

## Problem Statement
In real-life situations, patients often struggle to understand the severity of their symptoms based on vital signs such as blood pressure, heart rate, and oxygen level.

There is a need for a system that can:
- Analyze patient data
- Predict risk levels
- Detect emergency conditions
- Provide simple guidance

---

## Solution Approach
This project uses a **hybrid approach**:
- **Machine Learning (ML):** Predicts risk level based on patient data
- **Rule-Based AI Logic:** Refines predictions and detects emergencies
- **Risk Scoring System:** Assigns a score to quantify severity

---

## Technologies Used
- Python
- pandas
- scikit-learn
- pickle

---

## AI & ML Concepts Used
- Classification (Decision Tree Model)
- Feature-based prediction
- Rule-based reasoning (AI)
- Risk scoring system
- Basic data preprocessing

---

## Project Structure

| File | Description |
|------|-------------|
| `data_generator.py` | Generates dataset |
| `dataset.csv` | Patient dataset |
| `model.py` | Trains ML model |
| `model.pkl` | Saved trained model |
| `predict.py` | Prediction module |
| `decision_logic.py` | Rule-based AI system |
| `main.py` | Main execution file |
| `README.md` | Project documentation |
| `statement.md` | Project explanation |

---

## Environment Setup

### Step 1: Install Python
Make sure Python is installed (version **3.x** recommended). Check using:
```bash
python --version
```

### Dependencies Installation
Install required libraries:
```bash
pip install pandas scikit-learn
```

### Configuration Steps
No additional configuration is required. Ensure all files are in the same folder:
- `dataset.csv`
- `model.pkl`
- Python scripts

---

## Execution Steps
Follow these steps in order:

### Step 1: Generate Dataset
```bash
python data_generator.py
```

### Step 2: Train the Model
```bash
python model.py
```
This will create: `model.pkl`

### Step 3: Run the System
```bash
python main.py
```

---

## Sample Input
```text
Age: 50
Gender: M
Blood Pressure: 150
Heart Rate: 95
SpO2: 92
BMI: 27
Temperature: 101
Smoker: 1
Activity: medium
Duration: 3
Symptom severity: 7
```

---

## Output Explanation
The system provides:
- **ML Prediction** → Initial risk prediction
- **Final Risk** → Adjusted risk after AI logic
- **Risk Score (0–100)** → Severity measure
- **Advice** → Suggested action

### Example:
```text
ML Prediction: Medium
Final Risk: High
Risk Score: 65
Advice: Emergency: Immediate medical attention required
```

---

## Project Report
The complete project report is available in this repository as `Project_Report.pdf`.

> If the preview is not visible on GitHub, please download the file and open it locally for full content.

---

## System Workflow
1. User enters patient details
2. Data is processed and converted
3. Machine Learning model predicts risk
4. Rule-based system checks critical conditions
5. Risk score is calculated
6. Final output and advice are displayed

---

## Key Features
- Machine learning-based prediction
- Rule-based decision system
- Risk scoring mechanism
- Emergency detection
- Simple CLI interface
- Modular code structure

---

## Use Case
This system can be useful for:
- Basic health monitoring
- Educational purposes
- Understanding AI in healthcare
- Early risk awareness

---

## Limitations
- Uses synthetic dataset
- Not a replacement for medical diagnosis
- Accuracy depends on data quality

---

## Future Improvements
- Real hospital dataset integration
- GUI-based interface
- Mobile/web application
- Deep learning models

---

## Author
**Atharva Dwivedi**

- **Registration Number:** 25III10240
- **Institution:** VIT Bhopal University
- **Program:** Integrated M.Tech AI

### Interests & Focus Areas
- Artificial Intelligence in Healthcare
- Bioinformatics & Medical Data Analysis
- Data Structures & Data Science

### Career Vision
To leverage AI and data-driven technologies to revolutionize healthcare systems and improve human life.

---

## Important Note
This project is developed for **academic purposes** to demonstrate the use of AI and Machine Learning concepts in healthcare systems.

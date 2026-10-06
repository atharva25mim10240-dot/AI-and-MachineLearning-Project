import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

# For Loading dataset
data = pd.read_csv("dataset.csv")

# Convert categorical data
data["gender"] = data["gender"].map({"M": 0, "F": 1})
data["activity"] = data["activity"].map({"low": 0, "medium": 1, "high": 2})

# Input features (X) and output (y)
X = data.drop("risk", axis=1)
y = data["risk"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Creating model
model = DecisionTreeClassifier()

# Training model
model.fit(X_train, y_train)

# Saving model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved successfully!")
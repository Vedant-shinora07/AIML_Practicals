# Implement Logistic Regression in Python using the given datasets.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
iris = load_iris(as_frame=True)
df = iris.frame

print("First 5 rows:")
print(df.head())

print("\nShape:", df.shape)
print("Class names:", iris.target_names)

# Features and target
X = df.drop("target", axis=1)
y = df["target"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Output
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Graph
plt.figure(figsize=(6,4))
for label in y.unique():
    subset = df[df["target"] == label]
    plt.scatter(subset["sepal length (cm)"], subset["petal length (cm)"],
                label=iris.target_names[label])

plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Iris Dataset")
plt.legend()
plt.show()
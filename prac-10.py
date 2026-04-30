# Implement K means clustering algorithm for grouping the data into 2 clusters.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# ---------------- IRIS DATASET ---------------- #
iris = load_iris()
X_iris = iris.data
y_iris = iris.target

print("Iris shape:", X_iris.shape)
print("Features:", iris.feature_names)

# KMeans clustering
kmeans = KMeans(n_clusters=3, n_init=10, random_state=0)
labels = kmeans.fit_predict(X_iris)

# Silhouette score
score = silhouette_score(X_iris, labels)
print("Silhouette Score (Iris):", score)

# Plot clusters vs true labels
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.scatter(X_iris[:,0], X_iris[:,1], c=labels)
plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")
plt.title("K-Means Clusters (Iris)")

plt.subplot(1,2,2)
plt.scatter(X_iris[:,0], X_iris[:,1], c=y_iris)
plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")
plt.title("True Labels (Iris)")

plt.show()


# ---------------- GLASS DATASET ---------------- #
print("\n--- Glass Dataset ---")

try:
    glass = pd.read_csv("glass.csv")
    print("Glass shape:", glass.shape)
    print("Glass types:", glass["Type"].unique())

    X_glass = glass.drop("Type", axis=1)

except:
    print("glass.csv not found → using dummy dataset")

    # Dummy dataset (backup for exam)
    data = {
        "RI":[1.5,1.6,1.7,1.8],
        "Na":[13,14,15,16],
        "Mg":[3,2,1,0],
        "Type":[1,2,3,1]
    }
    glass = pd.DataFrame(data)

    print("Glass shape:", glass.shape)
    print("Glass types:", glass["Type"].unique())

    X_glass = glass.drop("Type", axis=1)


# Elbow Method
inertia = []
k_range = range(2, len(X_glass) + 1)

for k in k_range:
    km = KMeans(n_clusters=k, n_init=10, random_state=0)
    km.fit(X_glass)
    inertia.append(km.inertia_)

# Plot Elbow graph
plt.plot(k_range, inertia, marker='o')
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method - Glass Dataset")
plt.show()
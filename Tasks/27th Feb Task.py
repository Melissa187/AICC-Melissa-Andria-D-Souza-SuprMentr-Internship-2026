#Today’s Task:
from sklearn.datasets import load_breast_cancer
#Steps:
#Train KNN classifier


#Try different K values (1–15)


#Plot Accuracy vs K


#Try Euclidean vs Manhattan


#Compare results


#Explain why accuracy changes with K

# KNN on Breast Cancer Dataset

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. Load dataset
data = load_breast_cancer()
X = data.data
y = data.target

# 2. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Try K values from 1 to 15
k_values = range(1, 16)
accuracies_euclidean = []
accuracies_manhattan = []

for k in k_values:
    # Euclidean Distance
    model_e = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    model_e.fit(X_train, y_train)
    y_pred_e = model_e.predict(X_test)
    acc_e = accuracy_score(y_test, y_pred_e)
    accuracies_euclidean.append(acc_e)

    # Manhattan Distance
    model_m = KNeighborsClassifier(n_neighbors=k, metric='manhattan')
    model_m.fit(X_train, y_train)
    y_pred_m = model_m.predict(X_test)
    acc_m = accuracy_score(y_test, y_pred_m)
    accuracies_manhattan.append(acc_m)

# 4. Print results
print("K  |  Euclidean  |  Manhattan")
print("--------------------------------")
for i in range(15):
    print(f"{i+1}  |  {accuracies_euclidean[i]:.4f}    |  {accuracies_manhattan[i]:.4f}")

# 5. Plot graph
plt.figure()
plt.plot(k_values, accuracies_euclidean)
plt.plot(k_values, accuracies_manhattan)
plt.xlabel("K Value")
plt.ylabel("Accuracy")
plt.title("Accuracy vs K for KNN")
plt.show()



#Project: Loan Approval Predictor Dataset columns: Income Credit Score Age Loan Amount Employment Years Steps: Load dataset Train Decision Tree Train Random Forest Compare accuracy Show feature importance Save model using pickle

# ==========================================
# LOAN DEFAULT PREDICTION (FINAL VERSION)
# ==========================================


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# -------------------------------
# 1. Load Dataset
# -------------------------------
data = pd.read_csv("loan_data.csv")


print("Dataset Loaded Successfully\n")
print("Class Distribution:")
print(data["not.fully.paid"].value_counts())


# -------------------------------
# 2. Convert Categorical Column
# -------------------------------
data = pd.get_dummies(data, columns=['purpose'], drop_first=True)


# -------------------------------
# 3. Define Features and Target
# -------------------------------
X = data.drop("not.fully.paid", axis=1)
y = data["not.fully.paid"]


# -------------------------------
# 4. Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


# -------------------------------
# 5. Decision Tree (Balanced)
# -------------------------------
dt_model = DecisionTreeClassifier(
    random_state=42,
    class_weight='balanced'
)


dt_model.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)


print("\n===== Decision Tree Results =====")
print("Accuracy:", accuracy_score(y_test, dt_pred))
print(classification_report(y_test, dt_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, dt_pred))


# -------------------------------
# 6. Random Forest (Balanced)
# -------------------------------
rf_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight='balanced'
)


rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)


print("\n===== Random Forest Results =====")
print("Accuracy:", accuracy_score(y_test, rf_pred))
print(classification_report(y_test, rf_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, rf_pred))


# -------------------------------
# 7. Feature Importance
# -------------------------------
importance = rf_model.feature_importances_
features = X.columns


importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
}).sort_values(by="Importance", ascending=False)


print("\nTop 10 Important Features:\n")
print(importance_df.head(10))


plt.figure()
plt.bar(importance_df["Feature"][:10], importance_df["Importance"][:10])
plt.xticks(rotation=90)
plt.title("Top 10 Feature Importance")
plt.show()


# -------------------------------
# 8. Save Final Model
# -------------------------------
with open("loan_default_model.pkl", "wb") as f:
    pickle.dump(rf_model, f)


print("\nFinal Model saved as loan_default_model.pkl")


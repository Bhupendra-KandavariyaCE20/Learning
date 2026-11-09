import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

data = {
    "tenure_months": [3, 24, 6, 36, 2, 18, 12, 48, 5, 30, 1, 60, 8, 15, 42],
    "monthly_charges": [
        950,
        500,
        850,
        400,
        990,
        600,
        750,
        350,
        900,
        450,
        1050,
        300,
        800,
        650,
        380,
    ],
    "support_tickets": [5, 1, 4, 0, 6, 2, 3, 0, 4, 1, 7, 0, 5, 2, 0],
    "churn": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
}

features = ["tenure_months", "monthly_charges", "support_tickets"]
df = pd.DataFrame(data)

X = df[features]
y = df["churn"]
print(X.head())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)

print("Training Completed")

# Predict classes
predictions = model.predict(X_test)

# Predict probabilities
probabilities = model.predict_proba(X_test)


print("Predictions:")
print(predictions)

print("Probabilities:")
print(probabilities)

print(f"Model classes {model.classes_}")

threshold = 0.3
churned_prob = model.predict_proba(X_test)[:, 1]
custom_predictions = (churned_prob >= threshold).astype(int)

print(custom_predictions)

classifier = model.named_steps["logisticregression"]

print("Intercept:", classifier.intercept_)

coefficients = pd.DataFrame({"Feature": features, "Coefficient": classifier.coef_[0]})

print(coefficients)

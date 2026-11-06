## Sample Data for Customer Churn Prediction
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

data = [
    {
        "customer_id": "C001",
        "tenure_months": 2,
        "monthly_charges": 79.5,
        "contract_type": "monthly",
        "support_tickets": 4,
        "churned": 1,
    },
    {
        "customer_id": "C002",
        "tenure_months": 24,
        "monthly_charges": 65.0,
        "contract_type": "yearly",
        "support_tickets": 1,
        "churned": 0,
    },
    {
        "customer_id": "C003",
        "tenure_months": 3,
        "monthly_charges": 90.0,
        "contract_type": "monthly",
        "support_tickets": 5,
        "churned": 1,
    },
    {
        "customer_id": "C004",
        "tenure_months": 48,
        "monthly_charges": 55.0,
        "contract_type": "two_year",
        "support_tickets": 0,
        "churned": 0,
    },
    {
        "customer_id": "C005",
        "tenure_months": 7,
        "monthly_charges": 82.0,
        "contract_type": "monthly",
        "support_tickets": 3,
        "churned": 1,
    },
    {
        "customer_id": "C006",
        "tenure_months": 36,
        "monthly_charges": 60.0,
        "contract_type": "yearly",
        "support_tickets": 1,
        "churned": 0,
    },
    {
        "customer_id": "C007",
        "tenure_months": 12,
        "monthly_charges": 75.0,
        "contract_type": "monthly",
        "support_tickets": 2,
        "churned": 1,
    },
    {
        "customer_id": "C008",
        "tenure_months": 2,
        "monthly_charges": 95.0,
        "contract_type": "monthly",
        "support_tickets": 6,
        "churned": 1,
    },
    {
        "customer_id": "C009",
        "tenure_months": 60,
        "monthly_charges": 50.0,
        "contract_type": "two_year",
        "support_tickets": 0,
        "churned": 0,
    },
    {
        "customer_id": "C010",
        "tenure_months": 18,
        "monthly_charges": 68.0,
        "contract_type": "yearly",
        "support_tickets": 2,
        "churned": 0,
    },
    {
        "customer_id": "C011",
        "tenure_months": 5,
        "monthly_charges": None,
        "contract_type": "monthly",
        "support_tickets": 4,
        "churned": 1,
    },
    {
        "customer_id": "C012",
        "tenure_months": 42,
        "monthly_charges": 58.0,
        "contract_type": "two_year",
        "support_tickets": 1,
        "churned": 0,
    },
    {
        "customer_id": "C013",
        "tenure_months": 9,
        "monthly_charges": 88.0,
        "contract_type": "monthly",
        "support_tickets": 3,
        "churned": 1,
    },
    {
        "customer_id": "C014",
        "tenure_months": 30,
        "monthly_charges": 62.0,
        "contract_type": "yearly",
        "support_tickets": 1,
        "churned": 0,
    },
    {
        "customer_id": "C015",
        "tenure_months": 54,
        "monthly_charges": 53.0,
        "contract_type": "two_year",
        "support_tickets": 0,
        "churned": 0,
    },
    {
        "customer_id": "C016",
        "tenure_months": 15,
        "monthly_charges": 72.0,
        "contract_type": "monthly",
        "support_tickets": 2,
        "churned": 1,
    },
]


df = pd.DataFrame(data)

# Drop customer_id from the df
df.drop(columns=["customer_id"], inplace=True)
print(df.head(2))

print(f"DataFrame Shape {df.shape}")


print("\nDataFrame Types")
print(df.info())


print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicated Records")
print(df.duplicated().sum())

print("\nStatistical Summary")
print(df.describe())


numerical_columns = ["tenure_months", "monthly_charges", "support_tickets"]
print("\nNumerical Columns Summary")
print(df[numerical_columns].describe())


print("\nAnalyse Categorical Feature")
print(df["contract_type"].value_counts())


print("\nVisualizing the Distribution of Numerical Features")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
sns.histplot(data=df, x="monthly_charges", kde=True, ax=axes[0])
sns.boxplot(data=df, x="monthly_charges", ax=axes[1])
plt.tight_layout()
plt.show()


print("\nCorrelation Analysis")
correlation = df[numerical_columns].corr(method="spearman")
sns.heatmap(correlation, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()

imputer = SimpleImputer(strategy="median")
charges = df[["monthly_charges"]]
imputed_charges = imputer.fit_transform(charges)
print(imputed_charges)


encoder = OneHotEncoder(handle_unknown="ignore")
encoded = encoder.fit_transform(df[["contract_type"]])
print(encoded.toarray())

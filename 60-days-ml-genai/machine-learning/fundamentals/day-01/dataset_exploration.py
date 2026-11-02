import pandas as pd


data = [
    {"customer_id": "C001", "tenure_months": 2, "monthly_charges": 79.5, "contract_type": "monthly", "support_tickets": 4, "churned": 1},
    {"customer_id": "C002", "tenure_months": 24, "monthly_charges": 65.0, "contract_type": "yearly", "support_tickets": 1, "churned": 0},
    {"customer_id": "C003", "tenure_months": 3, "monthly_charges": 90.0, "contract_type": "monthly", "support_tickets": 5, "churned": 1},
    {"customer_id": "C004", "tenure_months": 48, "monthly_charges": 55.0, "contract_type": "two_year", "support_tickets": 0, "churned": 0},
    {"customer_id": "C005", "tenure_months": 7, "monthly_charges": 82.0, "contract_type": "monthly", "support_tickets": 3, "churned": 1},
    {"customer_id": "C006", "tenure_months": 36, "monthly_charges": 60.0, "contract_type": "yearly", "support_tickets": 1, "churned": 0},
    {"customer_id": "C007", "tenure_months": 12, "monthly_charges": 75.0, "contract_type": "monthly", "support_tickets": 2, "churned": 1},
    {"customer_id": "C008", "tenure_months": 2, "monthly_charges": 95.0, "contract_type": "monthly", "support_tickets": 6, "churned": 1},
    {"customer_id": "C009", "tenure_months": 60, "monthly_charges": 50.0, "contract_type": "two_year", "support_tickets": 0, "churned": 0},
    {"customer_id": "C010", "tenure_months": 18, "monthly_charges": 68.0, "contract_type": "yearly", "support_tickets": 2, "churned": 0},
    {"customer_id": "C011", "tenure_months": 5, "monthly_charges": None, "contract_type": "monthly", "support_tickets": 4, "churned": 1},
    {"customer_id": "C012", "tenure_months": 42, "monthly_charges": 58.0, "contract_type": "two_year", "support_tickets": 1, "churned": 0},
    {"customer_id": "C013", "tenure_months": 9, "monthly_charges": 88.0, "contract_type": "monthly", "support_tickets": 3, "churned": 1},
    {"customer_id": "C014", "tenure_months": 30, "monthly_charges": 62.0, "contract_type": "yearly", "support_tickets": 1, "churned": 0},
    {"customer_id": "C015", "tenure_months": 54, "monthly_charges": 53.0, "contract_type": "two_year", "support_tickets": 0, "churned": 0},
    {"customer_id": "C016", "tenure_months": 15, "monthly_charges": 72.0, "contract_type": "monthly", "support_tickets": 2, "churned": 1},
]

df = pd.DataFrame(data)

print(df.head())

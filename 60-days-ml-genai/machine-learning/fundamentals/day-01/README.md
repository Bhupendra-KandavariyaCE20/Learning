# Customer Churn Prediction: Dataset Exploration

## Problem Statement

Explore customer account data and prepare a machine-learning task to predict whether a customer will churn. The target records whether each customer left (`1`) or stayed (`0`).

## Dataset Description

The project uses a small, synthetic dataset defined directly in `dataset_exploration.py` and `dataset_exploration.ipynb`; it is not an externally sourced dataset. It contains 16 customer records and six columns:

| Column | Description | Role |
| --- | --- | --- |
| `customer_id` | Customer identifier | Identifier; excluded from model features |
| `tenure_months` | Length of the customer's service, in months | Numerical feature |
| `monthly_charges` | Customer's monthly charge | Numerical feature |
| `contract_type` | Contract category (`monthly`, `yearly`, or `two_year`) | Categorical feature |
| `support_tickets` | Number of support tickets | Numerical feature |
| `churned` | Whether the customer left (1) or stayed (0) | Target |

## Features and Target

The model input features are `tenure_months`, `monthly_charges`, `contract_type`, and `support_tickets`. The target is `churned`. `customer_id` is an identifier and is dropped before splitting. In the notebook, `contract_type` is label-encoded using the training data's fitted encoder, then the same encoder transforms the test data.

## ML Problem Type

This is a supervised binary classification problem: predict one of two target classes, churned (`1`) or stayed (`0`).

## Dataset Exploration Findings

- The dataset has 16 rows and 6 columns.
- There is one missing value in `monthly_charges`; all other columns have no missing values.
- There are no duplicate records.
- The target is balanced in this sample: 8 customers churned and 8 stayed (50% churn).
- In this small sample, all churned customers have monthly contracts, while all customers on yearly or two-year contracts stayed. Churned customers also generally have shorter tenure and more support tickets. These patterns are descriptive only and should not be treated as reliable generalizations from such a small synthetic dataset.
- The notebook identifies the missing charge but does not yet impute it. Handle missing values before fitting a model that cannot accept them.

## Training and Testing Split

The notebook uses scikit-learn's `train_test_split` with `test_size=0.25` and `random_state=42`, resulting in 12 training rows and 4 test rows. It drops `customer_id` and `churned` from the feature matrix and uses `churned` as the target. Although the notebook's task notes call for stratification, the current split call does not pass `stratify=y`; add that argument if the split must preserve the class proportions.

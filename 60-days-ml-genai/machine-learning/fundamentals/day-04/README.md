# Day 04: Exploratory Data Analysis and Data Preprocessing

This lesson focuses on preparing raw customer data for machine learning by exploring patterns, handling missing values, and transforming features into a model-ready format.

## Objectives

- Explore a tabular dataset for churn prediction
- Check missing values, duplicate records, and data types
- Understand basic descriptive statistics and feature distributions
- Use data visualization to inspect patterns and outliers
- Apply preprocessing techniques such as imputation, scaling, and one-hot encoding
- Build a preprocessing pipeline for machine learning

## Files

### eda.py
This script performs exploratory data analysis on a sample customer churn dataset.

It includes:
- loading data into a Pandas DataFrame
- removing non-essential identifiers
- checking data shape, types, and missing values
- summarizing numerical and categorical features
- visualizing value distributions
- calculating correlations
- demonstrating imputation, one-hot encoding, standard scaling, and min-max scaling

### transformer.py
This script builds a more realistic preprocessing workflow using scikit-learn pipelines and ColumnTransformer.

It covers:
- separating numerical and categorical features
- imputing missing values with appropriate strategies
- standardizing numeric columns
- one-hot encoding categorical columns
- combining preprocessing steps into a single pipeline
- splitting data into training and testing sets
- transforming the training and validation data ready for model training

## Dataset Example

The sample dataset contains customer attributes such as:
- tenure_months
- monthly_charges
- contract_type
- support_tickets
- churned

This is a simple supervised learning problem where the target is whether a customer churned.

## Key Concepts

### Exploratory Data Analysis
EDA helps us understand the dataset before modeling. It answers questions like:
- What does the data look like?
- Are there missing values or duplicates?
- Which features are categorical or numerical?
- Are there patterns or relationships between variables?

### Missing Value Handling
Real-world datasets often contain missing values. Common strategies include:
- median imputation for numerical columns
- most frequent value imputation for categorical columns

### Feature Scaling
Scaling makes numerical features comparable, especially for algorithms sensitive to feature magnitude.

Typical methods:
- StandardScaler
- MinMaxScaler

### One-Hot Encoding
Categorical features such as contract_type cannot be directly used by most ML algorithms in raw form. One-hot encoding converts them into binary indicator columns.

### Pipelines
Pipelines keep preprocessing steps organized and ensure the same transformations are applied consistently to train and test data.

## Example Run

```bash
python eda.py
python transformer.py
```

## Why This Matters

Before training a machine learning model, the data must be cleaned and transformed into a format that the model can learn from. This step is critical because poor preprocessing can reduce performance or create misleading results.

Day 04 introduces the practical workflow used in real ML projects: inspect data, clean it, transform it, and prepare it for modeling.

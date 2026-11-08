# Day 05: House Price Prediction with Linear Regression

This lesson introduces a simple supervised learning problem: predicting house price from house size using a linear regression model.

## Objectives

- Understand the basic workflow of a machine learning project
- Learn how to split data into training and testing sets
- Train a Linear Regression model
- Evaluate performance using error metrics
- Predict the price of a new house using the trained model
- Visualize the relationship between feature and target

## Files

### house_price_prediction.py
This is the main script for the day.

It performs the following steps:
- loads the dataset from `house_prices.csv`
- selects the feature column `house_size_sq_ft`
- sets the target as `price_in_lakh_inr`
- splits the dataset into training and test sets
- creates and trains a `LinearRegression` model
- evaluates the model using metrics such as:
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)
  - Mean Absolute Error (MAE)
  - R-squared ($R^2$)
- predicts the price for a new house size
- plots the actual observations and the regression line

### evaluate_model.py
This file is intended for model evaluation exercises and is part of the learning workflow for checking how well the regression model performs.

## Dataset

The dataset contains house attributes including:
- `house_size_sq_ft`
- `price_in_lakh_inr`

The model learns a relationship between house size and price using the equation:

$y = wx + b$

where:
- $x$ is the house size
- $w$ is the weight or coefficient
- $b$ is the intercept
- $y$ is the predicted price

## Example Run

```bash
python house_price_prediction.py
```

## Key ML Concepts

### Supervised Learning
The model is trained on labeled data, where the target value (price) is known.

### Train-Test Split
The dataset is divided into training and testing sets so the model can be evaluated on unseen data.

### Linear Regression
Linear Regression fits a straight line that best represents the relationship between input and target values.

### Model Evaluation
Model quality is measured using:
- MSE: average squared prediction error
- RMSE: square root of MSE
- MAE: average absolute prediction error
- $R^2$: proportion of variance explained by the model

## Why This Matters

This project is a foundational example of machine learning in regression tasks. It shows the standard workflow used in many real-world prediction systems: prepare data, train a model, evaluate it, and make predictions.

Day 05 builds the bridge from basic statistics and data preparation to real ML model training.

# Day 02: Linear Algebra and Basic ML Prediction

This folder introduces the core mathematical ideas used in machine learning: vectors, matrices, dot products, and simple prediction using weighted inputs.

## Objectives

- Understand basic vector and matrix operations
- Practice dot product and matrix multiplication
- Learn how a linear model computes predictions
- Validate input shapes before performing matrix operations

## Files

### linear_algebra.py
This script demonstrates:
- vector addition and subtraction
- element-wise multiplication
- scalar multiplication
- dot product calculation
- matrix addition, subtraction, multiplication, and transpose

### ml_prediction.py
This script builds a simple linear prediction example using NumPy. It defines:
- a feature matrix `X`
- a weight vector `weights`
- a bias value `bias`

The prediction is calculated using:

`y = X.dot(weights) + bias`

A shape check ensures the matrix multiplication is valid before computing the result.

## Example Run

```bash
python linear_algebra.py
python ml_prediction.py
```

## Key Concept

Machine learning models often use a linear form:

`y = Xw + b`

where:
- `X` is the input data
- `w` is the weight vector
- `b` is the bias term
- `y` is the predicted output

This lesson is the foundation for understanding how models learn and make predictions.

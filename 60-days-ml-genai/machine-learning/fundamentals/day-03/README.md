# Day 03: Descriptive Statistics and Probability

This folder focuses on the foundations of data analysis in machine learning: descriptive statistics, probability, and basic distributions.

## Objectives

- Understand measures of central tendency: mean, median, and mode
- Learn spread and variability: variance and standard deviation
- Explore percentiles and z-scores
- Understand experimental probability and normal distributions
- Practice simple statistical reasoning using NumPy and Python

## Files

### descriptive_statistics.py
This script covers summary statistics for a sample of billing/charges data.

It demonstrates:
- mean
- median
- standard deviation
- variance
- percentiles
- mode detection
- z-score based outlier detection

### des_statistics.py
This file provides a similar statistics exercise using Python logic and NumPy. It includes:
- descriptive metrics for a dataset
- percentile calculations
- z-scores
- outlier detection using a threshold of 2 standard deviations

### distribution.py
This script demonstrates experimental probability through simulated random events.

It includes:
- coin toss simulation
- dice roll probability
- comparison of experimental vs theoretical probability
- repeated sampling to observe convergence

### probability.py
This file focuses on probability concepts and random sampling.

It includes:
- basic probability examples
- random integer generation
- coin toss probability with different sample sizes
- normal distribution generation with `numpy.random.default_rng`
- z-score calculations for potential outliers

### test_statistics.py
This file contains a manual implementation of basic statistical functions in pure Python, including:
- mean
- median
- mode
- variance
- standard deviation

## Core Concepts

### Descriptive Statistics
Descriptive statistics summarize and explain the main features of a dataset.

Examples:
- `mean`: average value
- `median`: middle value
- `mode`: most frequent value
- `variance`: how spread out the data is
- `standard deviation`: square root of variance

### Probability
Probability measures the likelihood of an event occurring.

Examples:
- probability of heads in a fair coin toss = 0.5
- probability of rolling a number greater than 4 on a die = 2/6 = 0.333...

### Normal Distribution
A normal distribution is a bell-shaped curve commonly seen in real-world data. It is defined by:
- mean (`loc`)
- standard deviation (`scale`)

## Example Run

```bash
python descriptive_statistics.py
python des_statistics.py
python distribution.py
python probability.py
python test_statistics.py
```

## Why This Matters

Statistics and probability are essential in machine learning because they help us:
- understand datasets
- measure variability
- detect anomalies
- validate model assumptions
- reason about uncertainty

This lesson builds the foundation for more advanced ML topics such as data preprocessing, feature engineering, and model evaluation.

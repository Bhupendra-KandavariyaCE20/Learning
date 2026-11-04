import numpy as np
import matplotlib.pyplot as plt

total_customers = 1000
churned = 200

p_churn = churned / total_customers
p_not_churn = 1 - p_churn

print(p_churn)
print(p_not_churn)


# Numpy provides a random number generator (RNG) that can be used to generate random numbers. The default_rng() function creates a new instance of the default random number generator, which is based on the PCG64 algorithm. You can also specify a seed value to ensure reproducibility of the random numbers generated.
rng = np.random.default_rng(seed=42)

samples = rng.integers(low=1, high=7, size=10)

print(samples)


# coin toss
coin_toss = rng.choice([0, 1], size=1000, p=[0.5, 0.5])

total_heads = np.sum(coin_toss == 1)
print(f"Heads Probability: {total_heads / len(coin_toss)}")

# bigger sample size
coin_toss = rng.choice([0, 1], size=100000, p=[0.5, 0.5])
total_heads = np.sum(coin_toss == 1)
print(f"Heads Probability: {total_heads / len(coin_toss)}")


# Normal Distribution
data = rng.normal(loc=100, scale=15, size=10000)
# loc=100: Mean.
# scale=15: Standard deviation.
# size=10000: Number of samples.

plt.hist(data, bins=40, density=True)
plt.xlabel("Values")
plt.ylabel("Density")
plt.title("Normal Distribution")
plt.show()


values = np.array([90, 95, 100, 105, 110, 150])
mean = np.mean(values)
std = np.std(values)

z_scores = (values - mean) / std

outliers = values[abs(z_scores) > 2]
print("Z-scores:", z_scores)
print("Potential outliers:", outliers)

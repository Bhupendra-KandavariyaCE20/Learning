import numpy as np

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

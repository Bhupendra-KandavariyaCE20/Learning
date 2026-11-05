import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=42)

# 1000 sample coin tosses with a fair coin (p=0.5 for heads and p=0.5 for tails)
coin_toss = rng.choice([0, 1], size=1000, p=[0.5, 0.5])

# Experimental probability of heads.
total_heads = np.sum(coin_toss == 1)
print(f"Heads Probability: {total_heads / len(coin_toss)}")

# Simulate 10,000 six-sided dice rolls
roll_dices = rng.integers(low=1, high=7, size=10000)

# Calculate the number of rolls that result in a value greater than 4.
number_greater_than_4 = np.sum(roll_dices > 4)
print(
    f"Experimental Probability of rolling a number greater than 4: {number_greater_than_4 / len(roll_dices)}"
)
# Calculate the theoretical probability.
theoretical_prob = (
    2 / 6
)  # There are 2 numbers (5 and 6) out of 6 that are greater than 4.
print(f"Theoretical Probability: {theoretical_prob}")

# Compare experimental and theoretical results.
print(
    f"Difference: {abs((number_greater_than_4 / len(roll_dices)) - theoretical_prob)}"
)

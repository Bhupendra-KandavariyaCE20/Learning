import numpy as np

charges = np.array(
    [500, 600, 700, 550, 800, 650, 750, 900, 600, 700, 500, 850, 950, 650, 700]
)

print(f"Mean: {np.mean(charges)}")
print(f"Median: {np.median(charges)}")
print(
    f"Standard Deviation {np.std(charges)}"
)  # np.std() calculates population standard deviation by default.
print(
    f"Variance: {np.var(charges)}"
)  # np.var() calculates population variance by default.
print(
    f"Sample Standard Deviation {np.std(charges, ddof=1)}"
)  # np.std() calculates population standard deviation by default.
print(
    f"Sample Variance: {np.var(charges, ddof=1)}"
)  # np.var() calculates population variance by default.


# A percentile tells us the value below which a specified percentage of observations falls.
print(np.percentile(charges, 25))

# calculating mode

unique_values, count = np.unique(charges, return_counts=True)

mode = unique_values[np.argmax(count)]
print(f"Mode: {mode}")

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


monthly_charges = np.array(
    [
        500,
        550,
        600,
        620,
        650,
        680,
        700,
        720,
        750,
        780,
        800,
        820,
        850,
        900,
        950,
        1000,
        1050,
        1100,
        1200,
        1500,
    ]
)

print(f"25th Percentile: {np.percentile(monthly_charges, 25)}")
print(f"50th Percentile: {np.percentile(monthly_charges, 50)}")
print(f"75th Percentile: {np.percentile(monthly_charges, 75)}")
mean_ = np.mean(monthly_charges)
std_ = np.std(monthly_charges)
print(f"Mean: {mean_}")
print(f"Standard Deviation: {std_}")
print(f"Variance: {np.var(monthly_charges)}")
z_scores = (monthly_charges - mean_) / std_
print(f"Z-scores: {z_scores}")
print(f"Outliers: {monthly_charges[np.abs(z_scores) > 2]}")

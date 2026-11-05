import math

charges = [500, 600, 700, 550, 800, 650, 750, 900, 600, 700, 500, 850, 950, 650, 700]


def calculate_mean(data):
    return sum(data) / len(data)


def calculate_median(data):
    sorted_data = sorted(data)
    sz = len(sorted_data)
    return (
        sorted_data[sz // 2]
        if sz % 2 != 0
        else (sorted_data[sz // 2 - 1] + sorted_data[sz // 2]) / 2
    )


def calculate_mode(data):
    value_counts = {}
    for i in data:
        count = value_counts.get(i, 0)
        value_counts[i] = count + 1

    val, cnt_ = data[0], 1
    for value, count in value_counts.items():
        if cnt_ < count:
            val = value
            cnt_ = count
    return val
    # unique_values = set(data)
    # max_count = 0
    # mode = None
    # for value in unique_values:
    #     count = data.count(value)
    #     if count > max_count:
    #         max_count = count
    #         mode = value
    # return mode


def calculate_var(data):
    mean_ = calculate_mean(data)
    total = 0
    for i in data:
        total += (i - mean_) ** 2
    return total / len(data)


def calculate_std(data):
    var_ = calculate_var(data)
    return math.sqrt(var_)


print(f"Mean: {calculate_mean(charges)}")
print(f"Median: {calculate_median(charges)}")
print(f"Standard Deviation: {calculate_std(charges)}")
print(f"Variance: {calculate_var(charges)}")
print(f"Mode: {calculate_mode(charges)}")

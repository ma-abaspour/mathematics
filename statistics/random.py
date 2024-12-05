
# Linear congruential generator
def lcg(seed, a=1664525, c=1013904223, m=2**32, n=1000):
    random_numbers = []
    for _ in range(n):
        seed = (a * seed + c) % m
        random_numbers.append(seed / m)  # Normalize to [0, 1)
    return random_numbers

# Toss N coins
def toss(n):
    if not hasattr(toss, "state"):
        toss.state = 1
    random_numbers = lcg(toss.state, n=n)
    toss.state = (1664525 * toss.state + 1013904223 * n) % (2**32)
    return "".join("H" if num < 0.5 else "T" for num in random_numbers)

def histogram(numbers, bins=10, range=(0, 1)):
    counts = [0] * bins
    bin_width = (range[1] - range[0]) / bins
    for num in numbers:
        if num == range[1]:
            idx = bins - 1
        else:
            idx = int((num - range[0]) / bin_width)
        counts[idx] += 1
    return counts

# Chi Square Statistics
def chi_square(observed, expected):
    return sum((o - e) ** 2 / e for o, e in zip(observed, expected))

def uniformity_test(numbers, bins=10, critical_value=16.919, data_range=(0, 1)):
    observed = histogram(numbers, bins, data_range)
    expected = [len(numbers) / bins] * bins
    chi2 = chi_square(observed, expected)
    return chi2, chi2 < critical_value

# random_numbers = lcg(seed=120, n=100)
# chi2, is_uniform = uniformity_test(random_numbers, bins=10)
# print("Chi-Square Statistic:", chi2)
# print("Passes Uniformity Test:", is_uniform)
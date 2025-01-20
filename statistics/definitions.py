def mean(X):
  return sum(X)/len(X)

def weighted_mean(X, weights):
    if len(X) != len(weights):
        raise ValueError("X and weights must have the same length.")
    return sum(x * w for x, w in zip(X, weights)) / sum(weights)

def harmonic_mean(X):
    return len(X) / sum(1 / x for x in X)

def geometric_mean(X):
    product = 1
    for x in X:
        product *= x
    return product ** (1 / len(X))


def median(X):
    sorted_X = sorted(X)
    mid = len(sorted_X) // 2
    if len(sorted_X) % 2 == 1:
        return sorted_X[mid]
    return (sorted_X[mid - 1] + sorted_X[mid]) / 2

def mode(X):
    frequency = {}
    for x in X:
        frequency[x] = frequency.get(x, 0) + 1
    max_count = max(frequency.values())
    modes = [key for key, val in frequency.items() if val == max_count]
    if len(modes) == len(X):
        return None  # No mode if all values are equally frequent
    return modes if len(modes) > 1 else modes[0]

def mean_absolute_deviation(X):
    mu = mean(X)
    return sum(abs(x - mu) for x in X) / len(X)

def variance(X):
    mu = mean(X)
    squared_differences = [(x - mu) ** 2 for x in X]
    return sum(squared_differences) / len(X)

def standard_deviation(X):
    return variance(X) ** 0.5

def range_stat(X):
    return max(X) - min(X)

def percentile(X, p):
    sorted_X = sorted(X)
    k = (len(sorted_X) - 1) * (p / 100)
    f = int(k)
    c = f + 1
    if c < len(sorted_X):
        return sorted_X[f] + (k - f) * (sorted_X[c] - sorted_X[f])
    return sorted_X[f]

def interquartile_range(X):
    q1 = percentile(X, 25)
    q3 = percentile(X, 75)
    return q3 - q1

def covariance(X, Y):
    if len(X) != len(Y):
        raise ValueError("X and Y must have the same length.")
    mu_x = mean(X)
    mu_y = mean(Y)
    return sum((x - mu_x) * (y - mu_y) for x, y in zip(X, Y)) / len(X)

def correlation_coefficient(X, Y):
    if len(X) != len(Y):
        raise ValueError("X and Y must have the same length.")
    stddev_x = standard_deviation(X)
    stddev_y = standard_deviation(Y)
    if stddev_x == 0 or stddev_y == 0:
        return 0
    return covariance(X, Y) / (stddev_x * stddev_y)

def skewness(X):
    mu = mean(X)
    stddev = standard_deviation(X)
    n = len(X)
    return sum((x - mu) ** 3 for x in X) / (n * stddev ** 3)

def kurtosis(X):
    mu = mean(X)
    stddev = standard_deviation(X)
    n = len(X)
    return sum((x - mu) ** 4 for x in X) / (n * stddev ** 4) - 3

def z_score(X, value):
    mu = mean(X)
    stddev = standard_deviation(X)
    return (value - mu) / stddev

def exponential_moving_average(X, alpha):
    ema = [X[0]]
    for i in range(1, len(X)):
        ema.append(alpha * X[i] + (1 - alpha) * ema[-1])
    return ema

def simple_linear_regression(X, Y):
    if len(X) != len(Y):
        raise ValueError("X and Y must have the same length.")
    n = len(X)
    x_mean, y_mean = mean(X), mean(Y)
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(X, Y))
    denominator = sum((x - x_mean) ** 2 for x in X)
    slope = numerator / denominator
    intercept = y_mean - slope * x_mean
    return slope, intercept

def residual_sum_of_squares(X, Y, slope, intercept):
    return sum((y - (slope * x + intercept)) ** 2 for x, y in zip(X, Y))

def coefficient_of_variation(X):
    return (standard_deviation(X) / mean(X)) * 100

def gini_coefficient(X):
    sorted_X = sorted(X)
    n = len(X)
    cumulative_sum = sum((i + 1) * x for i, x in enumerate(sorted_X))
    total_sum = sum(sorted_X)
    return (2 * cumulative_sum) / (n * total_sum) - (n + 1) / n

def entropy(X):
  from math import log
  total = sum(X)
  probabilities = [x / total for x in X]
  return -sum(p * (log(p) if p > 0 else 0) for p in probabilities)

# def bootstrap_sample(X, n_samples):
#   return [X[int(len(X) * random())] for _ in range(n_samples)]


def confidence_interval_mean(X, confidence=0.95):
    import math
    mean_X = mean(X)
    stddev = standard_deviation(X)
    n = len(X)
    margin_error = 1.96 * (stddev / math.sqrt(n))  # For ~95% confidence level
    return (mean_X - margin_error, mean_X + margin_error)

def confidence_interval_mean(X, confidence=0.95):
    import math
    mean_X = mean(X)
    stddev = standard_deviation(X)
    n = len(X)
    margin_error = 1.96 * (stddev / math.sqrt(n))  # For ~95% confidence level
    return (mean_X - margin_error, mean_X + margin_error)

def outliers_iqr(X):
    q1 = percentile(X, 25)
    q3 = percentile(X, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return [x for x in X if x < lower_bound or x > upper_bound]

def cdf(X):
    sorted_X = sorted(X)
    n = len(X)
    return [(x, sum(1 for i in sorted_X if i <= x) / n) for x in sorted_X]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def permutations(n, r):
    return factorial(n) // factorial(n - r)

def root_mean_square(X):
    return (sum(x ** 2 for x in X) / len(X)) ** 0.5

def binomial_probability(n, k, p):
    return combinations(n, k) * (p ** k) * ((1 - p) ** (n - k))

def exponential_growth(a, b, x):
    e = 2.718281828459045
    return a * (e ** (b * x))



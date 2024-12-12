
def derivative(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)

# f = lambda x: x**2
# print(derivative(f, 3))

def integrate(func, a, b, n=1000):
    step = (b - a) / n
    total = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        total += func(a + i * step)
    return total * step

# f = lambda x: x**2
# print(integrate(f, 0, 1))

def limit(func, x, h=1e-5):
    return (func(x + h) + func(x - h)) / 2

# f = lambda x: x**2
# print(limit(f, 2))

def definite_sum(func, a, b):
    total = 0
    for i in range(a, b + 1):
        total += func(i)
    return total

# f = lambda x: x
# print(definite_sum(f, 1, 10))

def taylor_series(func, x, a, n):
    def nth_derivative(f, x, order):
        for _ in range(order):
            f = lambda z: derivative(f, z)
        return f(x)
    
    approximation = 0
    for i in range(n):
        term = (nth_derivative(func, a, i) * (x - a)**i) / math.factorial(i)
        approximation += term
    return approximation

# import math
# f = math.sin
# print(taylor_series(f, math.pi/4, 0, 5))

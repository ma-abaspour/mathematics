
def integer_part(x, b):
    count = 0
    while x >= b:
        x /= b
        count += 1
    while x < 1:
        x *= b
        count -= 1
    return count, x

def fractional_part(x, b, tolerance):
    frac = 0
    factor = 0.5
    while factor > tolerance:
        x **= 2
        if x >= b:
            frac += factor
            x /= b
        factor /= 2
    return frac

def logarithm(x, b, tolerance=1e-10):
    if x <= 0 or b <= 0 or b == 1:
        raise ValueError("x must be > 0, b must be > 0 and not equal to 1.")
    
    int_part, reduced_x = integer_part(x, b)
    frac_part = fractional_part(reduced_x, b, tolerance)
    return int_part + frac_part

# Example usage
x = 30
b = 2
print(f"log_{b}({x}) =", logarithm(x, b))

# import math
# print(math.log(30, 2))

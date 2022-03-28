"""
When solving a Trinomials, you will organise the equation as:
GCF(simplified_equation) = a + b + c

In order to solve this you will break down or decompose the value of b.
The two new values (for examples we will call these X and Y) of b must be equal to:
    - X*Y = a*c
    - X + Y = b

This program will be an algorithm for finding the decomposed values of b (the values of X and Y).
"""
from Greatest_Common_Factor import check_factors

def get_decomposed_b(a, b, c):
    z = a * c

    b_factors = check_factors(b)

    for factor in range(len(b_factors)):
        x = b_factors[factor]
        y = b_factors[-1 * (factor + 1)]

        print(f"{x}, {y}")

        if x + y == b and x * y == z:
            return [x, y]

    return None


print(get_decomposed_b(4, -4, -3))
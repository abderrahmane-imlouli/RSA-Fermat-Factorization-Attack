import math

def fermat_factor(n: int):
    """
    Factor n using Fermat's factorization method.

    Works best when the two prime factors are close together.
    """

    a = math.isqrt(n)

    if a * a < n:
        a += 1

    while True:
        b2 = a * a - n
        b = math.isqrt(b2)

        if b * b == b2:
            return a - b, a + b

        a += 1
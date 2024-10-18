import sympy as sp


def zero_to_infinity():
    i = 0
    while True:
        yield i
        i += 1


x = int(input())
for i in zero_to_infinity():
    if sp.isprime(6 * i - 1) and sp.isprime(x - (6 * i - 1)):
        print(6 * i - 1, x - (6 * i - 1))
        break
    if sp.isprime(6 * i + 1) and sp.isprime(x - (6 * i + 1)):
        print(6 * i + 1, x - (6 * i + 1))
        break

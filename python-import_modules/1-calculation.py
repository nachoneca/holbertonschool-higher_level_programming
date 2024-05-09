#!/usr/bin/python3

if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add, sub, mul, div
    resa = add(a, b)
    ress = sub(a, b)
    resm = mul(a, b)
    resd = div(a, b)
    print("{} + {}= {}".format(a, b, resa))
    print("{} - {}= {}".formar(a, b, ress))
    print("{} x {}= {}".format(a, b, resm))
    print("{} / {}= {}".format(a, b, resd))

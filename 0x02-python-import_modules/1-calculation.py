#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    i_add = add(a, b)
    i_subtract = sub(a, b)
    i_multiply = mul(a, b)
    i_divide = div(a, b)

    print("{} + {} = {}".format(a, b, i_add))
    print("{} - {} = {}".format(a, b, i_subtract))
    print("{} * {} = {}".format(a, b, i_multiply))
    print("{} / {} = {}".format(a, b, i_divide))

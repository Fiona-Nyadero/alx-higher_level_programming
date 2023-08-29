#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div_ans = a / b
    except (ZeroDivisionError, FloatingPointError):
        div_ans = None
    finally:
        print("Inside result: {}".format(div_ans))
    return div_ans

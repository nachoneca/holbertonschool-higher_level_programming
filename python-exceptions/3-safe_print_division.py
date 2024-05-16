#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b
    except (TypeError, ValueError, ZeroDivisionError, Exception):
        return None
    else:
        return div
    finally:
        print("Inside result: {}".format(div))

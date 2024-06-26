#!/usr/bin/python3

def safe_print_division(a, b):
    div = None
    try:
        div = a / b
    except (TypeError, ValueError, ZeroDivisionError, Exception):
        return None
    finally:
        print("Inside result: {}".format(div))
    return div

#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in range(x):
        try:
            if int(my_list[i]):
                print("{:d}".format(my_list[i]), end="")
                num += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print()
    return num


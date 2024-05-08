#!/usr/bin/python3
def uppercase(str):
    for i in str:
        char = ord(i)#gets ascci
        if char >= 97 and char <= 122:
            char -= 32#make lttrs MAYUS
        print("{:c}".format(char), end="")#prints every letter in MAYUS
    print()#prints NL

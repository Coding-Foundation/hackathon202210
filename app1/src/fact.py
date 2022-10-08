import math


def cmd_fact(n):
    if n < 0:
        return  "undefined"
    return str(math.factorial(n))

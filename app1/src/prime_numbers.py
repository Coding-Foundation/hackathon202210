from sympy import primerange

"""
Command: prime_numbers
Return a list of all the prime numbers inferior or equal to n
"""
def prime_numbers(n):
    return primerange(0, n)


"""
Command: sum_prime_numbers
Return a sum of all the prime numbers inferior or equal to n
"""
def sum_prime_numbers(n):
    return sum(prime_numbers(n))

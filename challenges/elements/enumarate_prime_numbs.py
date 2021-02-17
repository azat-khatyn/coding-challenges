"""
input = 18
output = [2, 3, 5, 7, 11, 13, 17]

"""
import math

def is_prime(numb):
    if numb == 0 or numb == 1:
        return False
    if numb == 2:
        return True
    if numb % 2 == 0:
        return False
    for x in range(3, math.ceil(math.sqrt(numb))+1, 2):
        if numb % x == 0:
            return False
    return True


def all_primes(number):
    primes = []
    for numb in range(2, number):
        if is_prime(numb):
            primes.append(numb)
    return primes



print(all_primes(18))


def sieve_primes(numb):
    primes = []
    is_it_prime = [False, False] + [True] * (numb-1)
    for p in range(2, numb+1):
        if is_it_prime[p]:
            primes.append(p)
            for i in range(p*2, numb+1, p):
                is_it_prime[i] = False
    return primes


print(sieve_primes(18))

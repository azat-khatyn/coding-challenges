import math

def is_prime(n):
    if n == 0 or n == 1:
        return "not prime"
    if n == 2:
        return "prime"
    # devide by 2 tp check for even numbers
    if n % 2 == 0:
        return "not prime"
    for odd in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % odd == 0:
            return "not prime"
    return "prime"


for n in range(100):
    print('Number %d is %s' % (n, is_prime(n)))



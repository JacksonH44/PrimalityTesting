import random
from re import A
import sympy

# Python representation of the fast powering algorithm in mod m
# @param: base integer a, testing integer n, modulus m
# @return: a^n (mod m)

def power(a, n, m):
    if (n == 0):
        return 1
    
    # If we compute power(a, 2k, m) --> (a^k)^2
    # If we compute power(a, 2k+1, m) --> ((a^k)^2)*a
    x = power (a, n//2, m)
    x = (x*x)%m
    return (x*a)%m if (n%2)==1 else x

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def fermatWitness(a, n):
    return not pow(a, n-1, mod=n) == 1

def fermat(n):
    i = 0
    while i < 10:
        a = random.randint(2, n-1)
        if gcd(n, a) == 1: # Relatively prime
            if fermatWitness(a, n):
                return False
            i += 1
    return True


if __name__ in '__main__':

    x = int(input())
    print('prime') if fermat(x) else print('not prime')


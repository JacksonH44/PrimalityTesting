import random
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

if __name__ in '__main__':
    correct = 0
    incorrect = 0
    ran = int(input("Enter the number of tests: "))
    primes = list(sympy.primerange(2, ran)) # Generate a list of primes 

    # The range we want to test numbers n up to
    for x in range(3, ran + 1):
        base = random.randint(2, x - 1) # Generate a random number as the base
        if power(base, x - 1, x) == 1: # Fast powering algorithm
            if x in primes: # Reference against our list of primes
                correct += 1
            else: # Pseudoprime
                incorrect += 1
        else:
            correct += 1 # Fermat's little theorem is always correct for non primes

    print("The accuracy of one Fermat test is {:.2f}%".format(correct/(correct + incorrect) * 100))

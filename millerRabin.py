import random
import math

## The Miller-Rabin Algorithm

def millerRabin(n):
    if n > 2 and n % 2 == 0:
        return 'composite'
    
    s = 0
    t = n - 1

    ## Factor n - 1 into a product of a power of 2 and an even number

    while t % 2 == 0:
        s += 1
        t //= 2

    ## Now we have n - 1 = (2^s)t for some t odd

    x = random.randint(1, n - 1)

    if pow(x, n - 1, n) != 1:  # Checking for Fermat's test
        return 'composite'

    for i in range(s):
        j = pow(2, i)
        x0 = pow(x, j*t, n)
        if x0 == 1:  # Divides a term in the expansion
            j = pow(2, i - 1)
            x1 = pow(x, j*t, n)
            if x1 != 1 and x1 != (n-1):  # Is a nontrivial solution
                return 'composite'
    
    return 'prime'


if __name__ in '__main__':
    userNum = int(input("Enter a number: "))

    print(millerRabin(userNum))
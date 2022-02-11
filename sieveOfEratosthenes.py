if __name__ in '__main__':
    n = int(input("Enter a number: "))
    prime = [True for i in range(n + 1)]
    
    p = 2
    # If the prime is greater than sqrt(n) it has already been found
    while (p*p <= n):
        if prime[p] == True:

            # Count the composites as multiples of p
            # if a composite number lower than p ** 2 exists it has already been found 
            for i in range(p ** 2, n + 1, p):
                prime[i] = False

        p += 1
    prime[0] = False
    prime[1] = False
    
    # Print the primes
    for j in range(n+1):
        if prime[j] == True:
            print(j, end=' ')

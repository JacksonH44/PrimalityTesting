# Introduction
This winter, I am a member of Western's Directed Reading Program. My presentation topic is on Primality Testing and implementing these algorithms in Python. I will update the repository as the project moves along. The presentation date is April 2nd, 2022.

# Setup Instructions
Clone the respository and run ```py -m pip install sympy``` (for Windows)

# Fermat's Little Theorem
Fermat's Little Theorem is a famous number theory result that says for any integers a and p, where p is prime, a to the power of (p - 1) is congruent to 1 mod p. This is a great way to test for primes. However, there are infinitely many pseudoprimes: composites that pass this test. The FermatsAlgo.py module computes one Fermat test in a vaccuum. It is fairly accurat, but obviously fails for Fermat pseudoprimes, including Carmichael numbers.

# Sieve of Eratosthenes
The Sieve of Eratosthenes is interesting aside from the fact that it is hard to pronounce. The Sieve dates back to early Greece and is used to compute all the prime numbers up to a certain range. It looks through a list of 2, ..., sqrt(n) numbers and marks all multiples of each as composite. The leftover numbers are all prime.

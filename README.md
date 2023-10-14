# Introduction
In the winter semester of 2022 at Western University, I was a member of the [Directed Reading Program](https://www.math.uwo.ca/undergraduate/current_students/directed_reading_program.html). My presentation topic was on Primality Testing and implementing these algorithms in Python. This work was presented on April 2, 2022 at the Western Undergraduate Reading Program Seminar.

# Requirements
* [Python3.6+](https://www.python.org/downloads/)
* [SymPy](https://www.sympy.org/en/index.html)

# Setup Instructions
Clone the respository and run ```py -m pip install sympy``` (for Windows)

# Fermat's Little Theorem
Fermat's Little Theorem is a famous number theory result that says for any integers a and p, where p is prime, a to the power of (p - 1) is congruent to 1 mod p. This is a great way to test for primes. However, there are infinitely many pseudoprimes: composites that pass this test. The FermatsAlgo.py module computes one Fermat test in a vaccuum. It is fairly accurat, but obviously fails for Fermat pseudoprimes, including Carmichael numbers.

# Sieve of Eratosthenes
The Sieve of Eratosthenes is interesting aside from the fact that it is hard to pronounce. The Sieve dates back to early Greece and is used to compute all the prime numbers up to a certain range. It looks through a list of 2, ..., sqrt(n) numbers and marks all multiples of each as composite. The leftover numbers are all prime.

# Miller-Rabin Test
The Miller-Rabin test is the gold standard for primality testing in cryptography. Based on the fact that the square root of a number over a prime finite field has no non-trivial square roots equivalent to 1, it has a probability of correctness of 3/4. 

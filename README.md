# Introduction
This winter, I am a member of Western's Directed Reading Program. My presentation topic is on Primality Testing and implementing these algorithms in Python. I will update the repository as the project moves along. The presentation date is April 2nd, 2022.

# Setup Instructions
Clone the respository and run ```py -m pip install sympy``` (for Windows)

# Fermat's Little Theorem
Fermat's Little Theorem is a famous number theory result that says for any integers a and p, where p is prime, a to the power of (p - 1) is congruent to 1 mod p. This is a great way to test for primes. However, there are infinitely many pseudoprimes: composites that pass this test. The FermatsAlgo.py script tries to test the probability that one Fermat test is correct up to some positive integer n.

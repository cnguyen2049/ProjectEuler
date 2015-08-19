
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from collections import Counter
primes_under_20 = [2,3,5,7,11,13,17,19]
def prime_factors(n):
    if n == 1:
        return []
    for prime in primes_under_20:
        if n % prime == 0:
            return [prime] + prime_factors(n / prime)
primes_needed = Counter()

for n in range(2,21):
    primes = Counter(prime_factors(n))
    print primes_needed
    primes_needed = primes_needed | primes
    print primes_needed

total = 1
for prime, amount in primes_needed.items():
    total *= prime ** amount

print total

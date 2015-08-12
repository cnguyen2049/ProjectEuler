
"""
def primes(limit):
    primes = []
    primes.append(2)
    for x in range(1,limit,2):
        isPrime = True
        j = 0
        while(primes[j]*primes[j]<=x):
            if(x % primes[j]==0):
                isPrime = False
                break
            j += 1
        if(isPrime):
            primes.append(x)
    return primes

print primes(20)
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

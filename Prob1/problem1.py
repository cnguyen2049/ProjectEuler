"""
Problem #1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 100
"""

from sys import argv

n = argv[1]


def problem1(n):
    """
    Find the sum of multiples of 3 and 5 less than n
    """
    n = int(n)
    answer = 0
    for n in range(0, n):
        if n % 3 == 0 or n % 5 == 0:
            answer += n
    return answer

print problem1(n)

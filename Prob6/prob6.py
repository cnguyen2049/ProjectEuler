"""
The sum of squares of the first ten natural is,

1^2 + 2^2 + ... + 10 ^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 +...+ 10)^2 = 55 ^2 = 3025

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
"""

def square_of_sum(num):
    num+=1
    total_sum = 0
    for n in range(1,num):
        total_sum += n
    sum_square = total_sum * total_sum
    return sum_square

def sum_of_square(num):
    num+=1
    total = 0
    for n in range(1,num):
        squared_val = n * n
        total += squared_val
    return total

print square_of_sum(100) - sum_of_square(100)

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
#check is it is a palindrome
def check_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

def produce_values():
    palindromes = []
    for x in range(100,999):
        for y in range(100,999):
            product = x * y
            if check_palindrome(product) == True:
                palindromes.append(product)
    return palindromes


answer = produce_values()

print max(answer)

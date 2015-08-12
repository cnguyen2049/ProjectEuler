from sys import argv

n = argv[1]

def problem1(n):
    """
    Find the sum of multiples of 3 and 5 less than n
    """
    n = int(n)
    answer = 0
    for n in range(0,n):
        if n % 3 == 0 or n % 5 == 0:
            answer += n
    return answer

print problem1(n)

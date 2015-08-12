def largest_factor(n):
    factor = []
    d = 2
    while n > 1:
        while n % d == 0:
            factor.append(d)
            n /= d
        d +=1
    return factor

answer = largest_factor(600851475143)
answer2 = largest_factor(40)
print answer2
print answer
max_value = max(answer)

print max_value



def getLCM(start, finish):
    lcm = start
    for i in range(1,finish):
        sum = lcm
        while(sum % i != 0):
            sum += lcm
        lcm = sum
    return lcm


print getLCM(1,20)

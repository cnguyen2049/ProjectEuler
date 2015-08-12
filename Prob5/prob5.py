def logic(num):
    state = 0
    for x in range(1,21):
        if(not (num % x == 0)):
            state = 0
            break
        else:
            state = 1
        print num
    return state

def smallestDivisible():
    num = 1
    valid = 0
    valid = logic(num)
    while(valid != 1):
        num = num + 1
        valid = logic(num)

    return num

print smallestDivisible()

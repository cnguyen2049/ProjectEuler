def fib():
    answer = 0
    first = 0
    second = 1
    while(second<4000000):
        temp = first
        first = second
        second = temp + first
        if second % 2 == 0:
            answer += second
    return answer

print fib()

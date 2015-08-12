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


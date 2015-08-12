is_prime = lambda x: all(x%i !=0 for i in range(int(x**0.5)+1)[2:])

def solver():
    count = 0
    number = 2
    while(count < 10001):
        if(is_prime(number)):
            count+=1
            answer = number
        number+=1
    return answer

print solver()

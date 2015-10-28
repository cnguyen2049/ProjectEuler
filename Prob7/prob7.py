"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""



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



is_prime = lambda x: all(x%i !=0 for i in range(int(x**0.5)+1)[2:])

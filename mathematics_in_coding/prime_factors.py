def isPrime(n):
    if n == 1:
        return False
    
    i = 2
    while(i*i <= n):
        if n%i == 0:
            return False
        i += 1

    return True

def prime_factors(num):
     
     for i in range(2, num+1):
        if isPrime(i):
            x = i
            while num%x == 0:
                print(i)
                x = x*i

n = int(input("Enter a Number : "))
prime_factors(n)



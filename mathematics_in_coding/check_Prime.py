
# Method 1: Time Complexity = O(n)
def isPrime(num):

    if num == 1:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
        
    return True 

# Method 2: Time Complexity = O(n^1/2) or O(√n)
def isPrime2(num):
    
    if num == 1:
        return False

    i = 2
    while i*i <= num :

        if num % i == 0:
            return False
        i += 1

    return True 

# Method 3 : time complexity O(√n) and space O(1)
def isPrime3(num):
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True 
    
    if num % 2 == 0 or num % 3 == 0:
        return False

    # All prime numbers greater than 3 can be written in the form of 6k ± 1
    i = 5
    while (i*i <= num):
        if num % i == 0 or num % (i+2) == 0:
            return False 
        i += 6
    return True

if __name__ == "__main__":
    # n = 1031
    n = 17
    print(f"Check wether {n} is a Prime ? ")
    print("True") if isPrime(n) else print("False")  # method 1
    print("True") if isPrime2(n) else print("False") # method 2
    print("True") if isPrime3(n) else print("False") # method 3

'''
method 3 explanation 
 Why start from 5 and use i and i+2?
All prime numbers greater than 3 can be written in the form of 6k ± 1 (because numbers divisible by 2 or 3 have already been filtered).

Ex: 5 = 6x1-1, 7 = 6x1+1, 11 = 6x2-1, 13 = 6x2+1, etc.

This loop checks if num is divisible by i or i+2 — that is, 6k-1 and 6k+1.

We increment by 6 (i += 6) each time to test the next pair (i, i+2).


'''
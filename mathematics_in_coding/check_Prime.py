
# Method 1: Time Complexity = O(n)
def isPrime(num):

    if num == 1:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
        
    return True 

# Method 2: Time Complexity = O(n^1/2)
def isPrime2(num):
    
    if num == 1:
        return False

    i = 2
    while i*i <= num :

        if num % i == 0:
            return False
        i += 1

    return True 

# Method 3 : 
def isPrime3(num):
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True 
    
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while (i*i <= num):
        if num % i == 0 or num % (i+2) == 0:
            return False 
        i += 6
    return True

if __name__ == "__main__":
    n = 1031
    print(f"Check wether {n} is a Prime ? ")
    print("True") if isPrime2(n) else print("False")
    print("True") if isPrime3(n) else print("False")


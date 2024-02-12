"""
You are given a number n. You need to recursively find the nth term of the series S that is given by:
S(n) = n+ n*(S(n-1)) and S(0) = 1

"""
def theSequence(n):
    #code here
    if n <= 0:
        return 1 
    else:
        return n + (n * theSequence(n-1))
        
num = 3        
print("Recursive solution : ",theSequence(num))

############################ using loop #########################
n = 3 
result =1 

for i in range(1,n+1):

    result = i + (i * result)

print(result)
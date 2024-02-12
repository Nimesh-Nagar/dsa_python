def fun(n):  # fun(1000)
    if n > 4000:
        return
    
    print(n)
    fun(n*2)
    print(n)
    
def fun1(x,y):
    if y == 0:
        return 0 

    return (x + fun1(x,y-1))
    
    
# print(fun1(6,3))

def fun2(x):
    if x == 0:
        return 
    else:
        print("a")
        return fun2(x-1)
        
        
# fun2(10)
        
        
def fun3(n):
    if n==0:
        return
    print(n%2)
    fun3(n//2)
    
# fun3(25)





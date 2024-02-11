def fun(n):
   
    if n == 0:
        return
    
    print(n)
    fun(n-1)
    print(n)

def fun2(n):

    if n == 0:
        return
    fun(n-1)
    print(n)
    fun(n-1)


# fun(3)
fun2(3)
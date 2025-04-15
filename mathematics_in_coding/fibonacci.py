def fibonacii(num):
    first = 1
    second = 0

    if num < 0:
        return "Number should be positive"
    
    print(second, end=" ")

    if num == 1:
        return
    
    
    
    print(first, end=' ')
    
 
    for cnt in range(3,num+1):
        current = first + second 
        second = first 
        first = current 
        print(current, end=" ")

    

fibonacii(9)
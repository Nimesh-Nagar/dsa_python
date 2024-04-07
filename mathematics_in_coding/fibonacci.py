def fibonacii(num):
    first = 0
    second = 1

    if num < 0:
        return "Number should be positive"
    
    elif num == 0:
        return first
    
    elif num == 1:
        return second
    
    else: 
        for cnt in range(2,num+1):
            temp = first + second 
            first = second 
            second = temp 
        return second

print(fibonacii(6))
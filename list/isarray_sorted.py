# 
def is_sorted(arr,n):
    inc = True
    dec = True 


    if n == 0 or n == 1:
        return 1 
        
    for idx in range(1,n):
        if arr[idx-1] > arr[idx]:
            inc = False 
        
        if arr[idx-1] < arr[idx]:
            dec = False 
        
    if inc or dec:
        return 1
    else: 
        return 0 
    
arr = [1,1,2,3,4,8,5]
size = len(arr)

print("output : ",is_sorted(arr, size))

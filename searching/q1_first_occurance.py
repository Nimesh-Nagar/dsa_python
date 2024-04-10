
# find the index of first occurance of number 

###################### Linear Search Approch ######################
def first_occurance(arr, x):
    
    for idx in range(0, len(arr)):
        if (arr[idx] == x):
            return idx
        
    return -1

###################### Binary Search Approch ######################

def first_occurance_b(arr, x):
    low = 0
    high = len(arr) - 1
    
    while (low <= high):
        mid = (low + high)//2
    
        if arr[mid] > x:
            high = mid - 1 
            
        elif arr[mid] < x: 
            low = mid + 1
            
        else:
            if (mid == 0 or arr[mid-1] != arr[mid]):
                return mid
            else:
                high = mid - 1 
                            
    return -1 


arr = [5, 10, 10, 20, 20, 40]
num = 20

idx = first_occurance(arr, num)
print(idx)

print(first_occurance_b(arr, num))





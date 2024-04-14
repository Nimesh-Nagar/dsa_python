# Better Approach

def first_occur_b(arr, x):
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

def last_occur_b(arr, n):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] > n:
            high = mid - 1
        elif arr[mid] < n:
            low = mid + 1
        else:
            if mid == len(arr) - 1 or arr[mid] != arr[mid+1]:
                return mid
            else:
                low = mid + 1
    
    return -1

# ----------- counts the occurance of a Given Number ------------------------
def b_count_occur(l , x):
    first = first_occur_b(l, x)
    
    if first == -1:
        return 0     
    else: 
        return last_occur_b(l, x) - first + 1


l = [10, 20, 20, 20, 30, 30]
print(l)
x = int(input("Enter Number to find Count : ")) 

cnt = b_count_occur(l , x)
print(f"{x} appears {cnt} Times")



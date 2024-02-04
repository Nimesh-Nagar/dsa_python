# Find secind largest element 

def second_largest_ele(arr):

    if not lst:
        return None
    
    else:
        first_large = arr[0]
        second_large = None 
        
        for i in range(1, len(arr)):
            if arr[i] > first_large:
                second_large = first_large
                first_large = arr[i]
            else: 
                second_large = arr[i]

        return second_large

lst = [10,5,20,8]
arr = [12, 35, 1, 10, 34, 1]

print("Largest element in list : ",second_largest_ele(arr))
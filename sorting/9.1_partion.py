# Partion of a given array 
# Time and space complexity is "theta(n)" . It is not efficient need to improve space complexity. 
"""
Nave Approch 
use 2 for loops and a temp array to store result  
1. iterate and check for val "less" than pivot_val. & add to temp array
2. iterate and check for val "more" than pivot_val. $ add to temp array
3. copy temp array ele to original array

"""

def partition(arr, p_idx):

    n = len(arr)
    arr[p_idx] , arr[n-1] = arr[n-1], arr[p_idx]
    temp = []

    for x in arr:
        if x <= arr[n-1]:
            temp.append(x)

    for x in arr:
        if x > arr[n-1]:
            temp.append(x)
    
    for i in range(len(arr)):
        arr[i] = temp[i]
        

arr = [5, 13, 6, 9, 12, 8, 11]
print("original array : ",arr)

partition(arr, 5)

print(arr)
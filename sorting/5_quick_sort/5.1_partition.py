# Nave approach for Partition of given array: it is a stable.
# partition is a subprocess of quick sort
# Time and space complexity is "theta(n)" . It is not efficient need to improve space complexity.
"""
Nave Approch 
use 2 for loops and a temp array to store result  
1. iterate and check for val "less" than pivot_val. & add to temp array
2. iterate and check for val "more" than pivot_val. $ add to temp array
3. copy temp array ele to original array

"""


def partion(arr, pivot_idx):
    n = len(arr)
    arr[pivot_idx], arr[n - 1] = arr[n - 1], arr[pivot_idx]

    temp = []
    for ele in arr:
        if ele <= arr[n - 1]:
            temp.append(ele)

    for ele in arr:
        if ele > arr[n - 1]:
            temp.append(ele)

    for idx in range(len(arr)):
        arr[idx] = temp[idx]


arr = [6, 13, 5, 9, 12, 8, 11]
print("original array : ", arr)

partion(arr, 5)
print("After : ", arr)

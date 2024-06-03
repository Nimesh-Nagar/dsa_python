"""
Inversion Count for an array indicates – how far (or close) the array is from being sorted. 
If the array is already sorted, then the inversion count is 0, but if the array is sorted in reverse order,
the inversion count is the maximum. 

Given an array a[]. 
Where two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
"""

#Nave Approch | Time complexity = O(n^2)
def getInversion(arr, n):
    count = 0 

    for i in range(n-1):
        for j in range(i+1, n):

            if arr[i] > arr[j]:
                count += 1

    return count



# Merge Sort approch  Time complexity = O( n*log(n) )
def count_inv(arr, l, r):
    res = 0 
    if (l < r):
        m = (l + r)//2

        res += count_inv(arr, l, m)
        res += count_inv(arr, m+1, r)
        res += count_merge(arr, l, m, r)
    
    return res

def count_merge(arr, low, mid, high):

    left = arr[low:mid+1]
    right = arr[mid+1:high+1]

    count, i, j, k = 0, 0, 0, low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            count += len(left) - i

        k += 1

    while i < len(left):
       
        arr[k] = left[i]
        i += 1
        k += 1
            

    while j < len(right):

        arr[k] = right[j]
        j += 1
        k += 1

    return count
        
arr =  [1, 20, 6, 4, 5]
# arr = [8, 4, 2, 1]

n = len(arr)
# print("Number of Inversions are : ",getInversion(arr,n))

print("Number of Inversion are : ",count_inv(arr, 0, n-1))

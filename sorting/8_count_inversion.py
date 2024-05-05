"""
Inversion Count for an array indicates – how far (or close) the array is from being sorted. 
If the array is already sorted, then the inversion count is 0, but if the array is sorted in reverse order,
the inversion count is the maximum. 

Given an array a[]. 
Where two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
"""

#Nave Approch
def getInversion(arr, n):
    count = 0 

    for i in range(n-1):
        for j in range(i+1, n):

            if arr[i] > arr[j]:
                count += 1

    return count


# arr =  [1, 20, 6, 4, 5]
arr = [8, 4, 2, 1]

n = len(arr)

print("Number of Inversions are : ",getInversion(arr,n))


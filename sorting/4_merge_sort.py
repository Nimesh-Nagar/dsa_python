# two sorted array is give merge it and sort it.

def merge_basic(a,b):
    res  = a + b
    res.sort()

    return res

def merge_efficient(a,b):
    res = []
    m = len(a)
    n = len(b)
    i = j = 0
    
    while i < m  and j < n:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    while i < m:
        res.append(a[i])
        i += 1

    while j < n:
        res.append(b[j])
        j += 1

    return res 

arr1 = [10, 15]
arr2 = [5, 6, 6, 20, 40]
print(f"Array1 {arr1} \nArray2 = {arr2}")

print(f"Sorted array : {merge_basic(arr1, arr2)}")

print(f"Merge Sort : {merge_efficient(arr1, arr2)}")


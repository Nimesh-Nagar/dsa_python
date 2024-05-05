#LOmuto Partion 
"""
consider last element as pivot_val and accordingly arrange 
left side smaller ele than pivot_val
right side larger ele than pivot_val

"""

def lomuto_partion(arr, low, high):
    pivot = arr[high]   # let last element is the partion / pivot value
    i = low - 1

    for j in range(high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1    # return index of pivot ele after partion.  

arr = [10, 80, 30, 90, 50, 70]
print("Before : ",arr)
low = 0
high = len(arr)-1

lomuto_partion(arr, low, high)
print("After Lomuto Partion")
print(arr)


# Quick sort using Lomuto Partion technique

def lomuto_partion(arr, start, end):
    pivot = arr[end]
    idx = start - 1 

    for itr in range(start,end):
        if arr[itr] <= pivot:
            idx += 1 
            arr[idx], arr[itr] = arr[itr], arr[idx]

    arr[idx+1], arr[end] = arr[end], arr[idx+1]

    return idx + 1 
 

def quick_sort(arr, start, end):
    if start < end:
        pivot_idx = lomuto_partion(arr, start, end)
        quick_sort(arr, start, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, end)

# unsorted_arr = [10, 80, 90, 40, 50, 70]
unsorted_arr = [8, 4, 7, 9, 3, 10, 5]
low  = 0
high = len(unsorted_arr) - 1 


print("Before : ",unsorted_arr)
quick_sort(unsorted_arr, low, high)

print("After : ",unsorted_arr)
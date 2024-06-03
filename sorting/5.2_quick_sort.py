# Quick sort using Hoarse partion 

def hoarse_partion(arr, start, end):
    pivot = arr[start]
    i = start - 1 
    j = end + 1 

    while True:
       
        i = i + 1
        while arr[i] < pivot:
            i = i + 1

        j = j - 1
        while arr[j] > pivot:
            j = j - 1

        if i >= j:
            return j 
        
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, start, end):
    
    if start < end:
        p_idx = hoarse_partion(arr, start, end)
        quick_sort(arr, start, p_idx)
        quick_sort(arr, p_idx+1, end)


arr = [8, 4, 7, 9, 3, 10, 5]
low = 0 
high = len(arr) - 1 

quick_sort(arr, low, high)

print(arr)
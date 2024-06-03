def merge_subarray(arr, low, mid, high):
    left = arr[low : mid + 1]
    right = arr[mid + 1 : high + 1]
    i = j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
            
        else:
            arr[k] = right[j]
            k += 1
            j += 1

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1

def merge_sort(arr, left, right):

    if right > left:
        mid = (right + left)//2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge_subarray(arr, left, mid, right)

arr = [10, 5, 30, 15, 7]
print(f"Original Array : {arr}")

low = 0 
high = len(arr) - 1
merge_sort(arr, low, high)

print(f"\nAfter Merge Sort : {arr}")

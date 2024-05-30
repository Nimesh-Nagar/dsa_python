# sort a given array using merge sort


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


a = [10, 15, 20, 40, 8, 11, 55]
low = 0
high = len(a) - 1
mid = (low + high ) //2

merge_subarray(a, low, mid, high)
print(a)

def merge_subarray(arr, low, mid, high):

    left = arr[low : mid+1]
    right = arr[mid+1 : high+1]
    i = j = 0
    k =low

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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

    while  j < len(right):
        k += 1
        i += 1
        arr[k] = right[j]

        k += 1
        i += 1


a = [10, 15, 20, 40, 8, 11, 55]

merge_subarray(a, 0, 3, 6)
print(a)


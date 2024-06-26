# Quick sort using Hoarse partition


def hoarse_partition(arr, start, end):
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
        p_idx = hoarse_partition(arr, start, end)
        quick_sort(arr, start, p_idx)
        quick_sort(arr, p_idx + 1, end)


unsorted_arr = [8, 4, 7, 9, 3, 10, 5]
print("Before : ", unsorted_arr)

low = 0
high = len(unsorted_arr) - 1
quick_sort(unsorted_arr, low, high)

print("After : ", unsorted_arr)

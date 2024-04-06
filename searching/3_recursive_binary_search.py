def bsearch(arr, n, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == n:
        return mid
    elif arr[mid] > n:
        return bsearch(arr, n, low, mid - 1)
    else:
        return bsearch(arr, n, mid + 1, high)


def bsearch_main(arr, num):
    return bsearch(arr, num, 0, len(arr) - 1)


sorted_arr = [10, 20, 30, 40, 50, 60, 70]
find_num = int(input("Enter the number to find : "))

index = bsearch_main(sorted_arr, find_num)

if index >= 0:
    print(f"Number {find_num} found at index {index}")
else:
    print(f"Number {find_num} not in array")

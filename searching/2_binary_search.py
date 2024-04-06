#


def binary_search(arr, num):
    low = 0
    high = len(arr) - 1

    while low <= high:
        # mid = (low + high) // 2
        mid = low + (high - low) // 2 
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1

    return -1


sorted_arr = [10, 20, 30, 40, 50, 60, 70]
find_num = int(input("Enter the number to find : "))

index = binary_search(sorted_arr, find_num)
if index >= 0:
    print(f"Number {find_num} found at index {index}")
else:
    print(f"Number {find_num} not in array")

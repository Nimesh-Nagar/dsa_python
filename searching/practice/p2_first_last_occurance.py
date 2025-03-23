def first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    first = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1  # Move left to find earlier occurrence
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first

def last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    last = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1  # Move right to find later occurrence
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last

def find_first_and_last(arr, target):
    first = first_occurrence(arr, target)
    last = last_occurrence(arr, target)
    return first, last

# Example Usage:
arr = [1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5]
target = 3
print(find_first_and_last(arr, target))  # Output: (6, 8)

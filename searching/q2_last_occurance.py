
###################### Linear Search Approch ######################
def last_occurance(arr, n):
    for idx in reversed(range(len(arr))):
        if arr[idx] == n:
            return idx
    return -1


###################### Binary Search Approch ######################

def last_occur_b(arr, n):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high)//2

        if n > arr[mid]:
            low = mid + 1
        elif n < arr[mid]:
            high = mid + 1

        else:
            if arr[mid] == len(arr) or arr[mid] != arr[mid+1]:
                return mid
            else:
                low = mid + 1



arr = [5, 10, 10, 20, 20, 40]
num = 20

# index = last_occurance(arr, num)

index = last_occur_b(arr, num)

if index >= 0:
    print(f"Last occurance of Number {num} found at index {index}")
else:
    print(f"Number {num} not in array")

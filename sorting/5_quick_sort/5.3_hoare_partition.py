# Hoare's Partion :: it is unstable
# faster than lomuto partion but time complexity is same
""" 
consider first element as pivot_val and accordingly arrange. 

time complexity theta(n), space complexity = O(1)
unstable 

"""


def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        # values less than pivot
        i += 1
        while arr[i] < pivot:
            i += 1

        # values greater than pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


arr = [10, 80, 50, 90, 30, 70]
print("Original arr : ", arr)

low = 0
high = len(arr) - 1
idx = hoare_partition(arr, low, high)

# print("After Hoare's partition : ",arr)
print("Pivot element at index = ", idx)

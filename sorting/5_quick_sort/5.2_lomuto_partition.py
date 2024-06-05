# lomuto partition : it is unstable
# partition is a subprocess of quick sort.
"""
consider last element as pivot_val and accordingly arrange 
left side smaller ele than pivot_val
right side larger ele than pivot_val

"""


def lumoto_partion(arr, low, high):
    pivot = arr[high]  # considering last element as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


arr = [10, 80, 50, 90, 30, 70]
print("Original arr : ", arr)

low = 0
high = len(arr) - 1
idx = lumoto_partion(arr, low, high)

print("\nAfter Lomuto Partion : ", arr)
print("Pivot element is on index = ", idx)

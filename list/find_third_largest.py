# Given an array, arr of positive integers. Find the third largest element in it. 
# Return -1 if the third largest element is not found.

def third_largest(arr):

    size = len(arr)
    if size < 3:
        return -1
    
    first = second = third = float('-inf')

    for ele in arr:
        if ele > first:
            third = second
            second = first
            first = ele
        
        elif first > ele > second:
            third = second
            second = ele

        elif second > ele > third:
            third = ele

    return first if third == float('-inf') else third

print(third_largest([10, 20, 4, 45, 99, 99, 33]))  # Output: 33
print(third_largest([5, 5, 5]))  # Output: 5
print(third_largest([1, 2]))  # Output: 2
print(third_largest([3, 3, 1, 2]))  # Output: 1
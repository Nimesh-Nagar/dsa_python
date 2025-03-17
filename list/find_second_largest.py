# Find the second largest element from the list 

# [Method 1] : Using two loops time complexity : theta(n) 
def get_second_max(arr):

    arr_len = len(arr)
    if arr_len <= 1:
        return "List must contain at least two elements"
    
    first_lar = second_lar = 0

    for i in range(arr_len):
        if arr[i] > first_lar:
            first_lar = arr[i]

    for i in range(arr_len):
        if arr[i] > second_lar and arr[i] < first_lar:
            second_lar = arr[i]

    return second_lar if second_lar != 0 else "No second largest element"
# time complexity if O(2n) == O(n)
# ---------------------------------------------------------------------
# Method 2 : using only one loop 

def second_max(arr):

    if len(arr) <= 1:
        return "List must contain at least two elements"
    
    largest = arr[0]
    second_lar = None 

    for ele in arr[1:]:
        if ele > largest:
            second_lar = largest
            largest = ele 
        
        elif ele != largest:
            if second_lar == None or second_lar < ele:
                second_lar = ele

    return second_lar

# arr = [10,5,20,8]
# arr = [5, 20, 12, 10, 20, 10, 12]
arr = [4,4]

# print("Second largest element in list : ",get_second_max(arr))
print("Second Largest element is : ",second_max(arr))
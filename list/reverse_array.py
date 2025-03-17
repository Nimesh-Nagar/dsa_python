# Reverse the given array 
def reverse_array(arr):
    start_idx = 0
    end_idx = len(arr) - 1 

   # check and swipe until start index is smaller than end index
    while start_idx < end_idx:
        arr[start_idx], arr[end_idx] = arr[end_idx] , arr[start_idx]
        start_idx += 1
        end_idx -= 1

    return arr     


arr = [1,2,3,4,5,6]
print("Original Array : ",arr)
print("Reversed array : ", reverse_array(arr))

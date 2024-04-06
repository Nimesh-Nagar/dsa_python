
def linear_search(arr, num):
    for index in range(0,len(arr)):
        if arr[index] == num:
            return index
    
    return -1
    

sorted_arr = [10, 20, 30, 40, 50, 60, 70]
find_num = int(input("Enter the number to find : "))

idx = linear_search(sorted_arr, find_num)

if idx >= 0:
    print(f"Number {find_num} found at index {idx}")
else:
    print(f"Number {find_num} not in array")
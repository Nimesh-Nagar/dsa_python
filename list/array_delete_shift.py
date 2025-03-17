def delete_from_array(arr, idx):
    n = len(arr)

    # Handle negative index
    # if idx < 0:
    #     idx += n
    
    # if 0 <= idx < n:
    #     while idx < n - 1:
    #         arr[idx] = arr[idx + 1]
    #         idx += 1
    #     arr[n - 1] = 0
    
    # return arr
    
    # Handle negative index
    if idx < 0:
        idx += n
    
    if 0 <= idx < n:
        arr = arr[:idx] + arr[idx+1:] + [0]
    
    return arr

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print("Original array:", arr)
    
    try:
        idx = int(input("Enter Index to be deleted: "))
        print("Updated array:", delete_from_array(arr, idx))
    except ValueError:
        print("Invalid input! Please enter an integer.")

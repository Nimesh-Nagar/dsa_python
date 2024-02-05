#

def delete_from_arry(arr, n, idx):
    # while idx < n-1:
    #     arr[idx] = arr[idx+1]
    #     idx += 1
            
    # arr[n-1] = 0
    # return arr

    arr = arr[:idx] + arr[idx+1:] + [0]
    return arr 
        


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    n = len(arr)
    
    idx = int(input("Enter Index : "))
    print(arr)
    print(delete_from_arry(arr, n, idx))

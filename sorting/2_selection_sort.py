# Selection Sort Algorithm

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[min_idx], arr[i] = arr[i], arr[min_idx]     

lst = [10, 5, 8, 20, 2, 18] 
print(f"Original Array : {lst}")

selection_sort(lst)

print(f"After Selection Sort : {lst}")
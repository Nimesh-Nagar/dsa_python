# Insertion sor algorithm

def insertion_sort(arr):
    
    for i in range(1,len(arr)):
        x = arr[i]
        j = i - 1

        while j >= 0 and x < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
            
        arr[j+1] = x

lst = [20, 5, 40, 60, 10, 30] 
print(f"Original Array : {lst}")

insertion_sort(lst)

print(f"After Selection Sort : {lst}")
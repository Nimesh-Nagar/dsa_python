# Hoare partion it is more efficient 
""" 
consider first element as pivot_val and accordingly arrange. 

time complexity theta(n), space complexity = O(1)
unstable 


"""

def hoare_partion(a, start, end):
    pivot = arr[start]
    i = start - 1
    j = end + 1 

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1 

        j -= 1 
        while arr[j] > pivot:
            j -= 1

        while i >= j:
            return j 
        
        arr[i], arr[j] = arr[j], arr[i]

arr = [5, 3, 8, 4, 2, 1, 10]
low = 0 
high = len(arr) - 1 

hoare_partion(arr, low, high)
print(arr)


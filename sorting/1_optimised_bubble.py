# optimised bubble sort

def opti_bubble_sort(lst):
    n = len(lst)
    
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True

        if swapped == False:
            return 


lst = [10, 8, 20, 5]
print(f"Original List : {lst}")

opti_bubble_sort(lst)
print(f"Sorted List : {lst}")
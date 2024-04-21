# Bubble sort

def bubble_sort(lst):
    n = len(lst)

    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp 

                # lst[j], lst[j+1] = lst[j+1], lst[j]


lst = [10, 8, 20, 5]
print(f"Original List : {lst}")

bubble_sort(lst)
print(f"Sorted List : {lst}")
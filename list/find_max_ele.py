# Find the largest element from list 

def largest_ele(lst):

    if not lst:
        return None
    
    else:
        largest = lst[0]
        for i in range(1,len(lst)):
            if lst[i] > largest:
                largest = lst[i]

        return largest

lst = [10,5,20,8]

print("Largest element in list : ",largest_ele(lst))

# Find the second largest element from the list 

# [Method 1] : Using two loops time complexity : theta(n) 
def get_second_max(arr):

    if len(arr) <= 1:
        return None
    
    first_lar = getmax(arr)
    second_lar = None 

    for x in arr:
        if x != first_lar:
            if second_lar == None:
                second_lar = x 
            else:
                second_lar = max(second_lar, x)

    return second_lar
    
def getmax(lst):
    large = lst[0]
    for ele in range(1, len(lst)):
        if lst[ele] > large:
            large = lst[ele]
    return large

# ---------------------------------------------------------------------
# Method 2 : using only one loop 

def second_max(arr):

    if len(arr) <= 1:
        return None
    
    lar = arr[0]
    slar = None 

    for x in arr[1:]:

        if x > lar:
            slar = lar
            lar = x 
        
        elif x != lar:
            if slar == None or slar < x:
                slar = x

    return slar

arr = [10,5,20,8]
# arr = [5, 20, 12, 10, 20, 10, 12]

# print("Largest element in list : ",get_second_max(arr))
print("Second Largest element is : ",second_max(arr))
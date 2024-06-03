
def intersection(a, b, len_a, len_b):
    i = j = 0
    while i < len_a and j < len_b:
        if i > 0 and a[i] == a[i-1]:
            i = i+1
            continue
        if(a[i]<b[j]):
            i=i+1 
        elif(b[j]<a[i]):
            j=j+1 
        else:
            print(a[i], end=" ")
            i=i+1 
            j=j+1 
       

arr1=[10, 20, 35, 40]
arr2=[20, 35, 50, 90]
intersection(arr1, arr2, len(arr1), len(arr2))
# Naive Approach
def count_occur(arr, x):
    count = 0
    for idx in range(len(arr)):
        if arr[idx] == x:
            count += 1

    return count

l = [10, 20, 20, 20, 30, 30]
print(l)
x = int(input("Enter Number to find Count : ")) 

cnt = count_occur(l,x)

print(f" {x} occurs {cnt} Times") 


def find_first_last(arr, x):
    n = len(arr)

    first = -1
    last = -1

    for index in range(0,n):
        if (x != arr[index]):
            continue
        if (first == -1):
            first = index

        last = index

    if (first != -1):
        print(f" First Occurance at {first} index \
              \n Last Occurance at {last} index ")
    else:
        print("Not Found")


arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
print(arr)
find_num = int(input("Enter Number to find : "))


find_first_last(arr, find_num)
"""
In this problem, we are given two sorted arrays and we need to find the union of both arrays,

i.e. we need to merge both arrays such that the elements which are present in both arrays 
should present only once in our answer.
"""


def union_sort(a, b):
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if i > 0 and a[i] == a[i - 1]:
            i += 1
        elif j > 0 and b[j] == b[j - 1]:
            j += 1

        elif a[i] < b[j]:
            print(a[i], end=" ")
            i += 1

        elif b[j] < a[i]:
            print(b[j], end=" ")
            j += 1

        else:
            print(a[i], end=" ")
            i += 1
            j += 1

    while i < len_a:
        if i > 0 and a[i] != a[i - 1]:
            print(a[i], end=" ")
            i += 1

    while j < len_b:
        if j > 0 and b[j] != b[j - 1]:
            print(b[j], end=" ")
            j += 1


a = [2, 10, 20, 20]
b = [2, 3, 20, 4]
# [2,3,4,10,20]

union_sort(a, b)

# Sort the array using insertion sort


class Solution:
    def insert(self, alist, index, n):
        # code here
        temp = alist[index]
        j = index - 1

        while j >= 0 and temp < alist[j]:
            alist[j + 1] = alist[j]
            j -= 1

        alist[j + 1] = temp

    # Function to sort the list using insertion sort algorithm.
    def insertionSort(self, alist, n):
        # code here
        for i in range(1, n):
            self.insert(alist, i, n)

        return alist


obj = Solution()

arr = [4, 1, 3, 9, 7]
size = len(arr)

print(f"Original Array : {arr}")
res = obj.insertionSort(arr, size)
print(f"After Insertion Sort : {res}")

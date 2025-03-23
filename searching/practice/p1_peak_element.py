'''
Given an array arr[] where no two adjacent elements are same, find the index of a peak element. An element is considered to be a peak if it is greater than its adjacent elements (if they exist). If there are multiple peak elements, return index of any one of them. 
The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".

Note: Consider the element before the first element and the element after the last element to be negative infinity.
'''

class Solution:   
    def peakElement(self,arr):
        # Code here
        left = 0 
        right = len(arr) - 1 
        

        while left <= right:
            mid = left + ( (right-left)//2 )
            
            #left element is greater
            if mid > 0 and arr[mid] < arr[mid-1]:
                right = mid - 1

            # right element is greater
            elif mid < len(arr)-1 and arr[mid] < arr[mid+1]: 
                left = mid + 1
            
            else:
                return mid
                
        return -1
    
obj = Solution()

ans = obj.peakElement([1, 2, 4, 5, 7, 8, 3])
ans1 = obj.peakElement([1, 2, 3])


print(ans1)
print(ans)

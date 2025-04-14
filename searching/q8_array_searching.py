""" 
Given an array arr. Your task is to find the elements whose value is equal to that of its index value ( Consider 1-based indexing ).

Note: There can be more than one element in the array which have the same value as its index. 
You need to include every such element's index. Follows 1-based indexing of the array.""" 

class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        res = []

        for idx in range(len(arr)):
            if arr[idx] == idx+1:
                res.append(arr[idx])
                
        return res        
            
ans = Solution()

print(ans.valueEqualToIndex([1]))
print(ans.valueEqualToIndex( [15, 2, 45, 4 , 7] ) ) # [2, 4] as index of 2 and 4 are same as there value 
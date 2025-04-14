"""
Given a binary array arr[], which is sorted in non-increasing order, 
count the number of 1's in it. 
""" 

def count_ones(arr):
   left = 0
   right = len(arr) - 1
    
   while left <= right:
      mid = left + (right - left) // 2
        
      if arr[mid] == 1:
         left = mid + 1  # Move right to find the last occurrence of 1
      else:
         right = mid - 1  # Move left since all 1s are before this

   return left  # The count of 1s 
        
arr = [1, 1, 1, 0, 0]

print(count_ones(arr))

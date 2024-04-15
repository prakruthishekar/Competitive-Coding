# Suppose an array of length n sorted in ascending order 
# is rotated between 1 and n times. For example, the array 
# nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 
# time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return 
# the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 





# Intuition
# The input array is monotonically increasing until it drops, then it 
# continues to monotonically increase. We want to find the point where 
# it drops (since the smallest element is located there).

# If there is no drop, then the first element is the lowest.

def findMin(nums) -> int:
        high, low = len(nums) - 1, 0
        while low < high - 1:
            mid = (high + low)//2
            if nums[low] > nums[mid]: 
                high = mid
            else: # drop must be to the left
                low = mid

        if nums[high] > nums[low]:
            return nums[0]
        return nums[high]


# def findMin(nums) -> int:
#         if(len(nums) == 0 ):
#             return 0
        
#         if(len(nums) == 1):
#             return nums[0]
        
#         minValue = float('inf')
#         left = 0
#         right = len(nums) - 1
#         while(left < right):
#             if(nums[left] >= nums[right]):
#                 minValue = min(minValue, nums[right])
#                 left += 1
#                 right -+ 1 
#             else:
#                 minValue = min(minValue, nums[left])
#                 left += 1
#                 right -+ 1

#         return minValue         

print(findMin([3,4,5,1,2]))  
print(findMin([1,2,3,4,5]))        

# Given an array of positive integers nums and a positive integer target, return the minimal length 
# of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.


# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Input: target = 7, nums = [1,2,3,4,5]
# Output: 11
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.


# Input: target = 4, nums = [1,4,4]
# Output: 1


# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

import sys

class Solution:	
    def minSubArrayLen(self, nums, target):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        self.target = target
        window_start = 0
        window_sum = 0
        minimum = sys.maxsize
        for window_end in range(len(nums)):
            window_sum += nums[window_end]   #add the next element  
# shrink the window as small as possible until the window_sum is smaller than target    
            while window_sum >= target:            
                window_sum -= nums[window_start]   #subtract the element going out
                minimum = min(minimum, window_end - window_start + 1)
                window_start += 1 # slide the window ahead
        return 0 if(minimum == sys.maxsize) else minimum

nums = [1,11,3,4,5]
target = 11
classObject = Solution()
print("Original Array", nums)
print("The contiguous subarray (containing at least one number) which has the largest sum and return its sum ", classObject.minSubArrayLen(nums,target))

#Time Complexity : O(n)    
# Kadane’s algorithm solution in python

# class Solution:
#     def maxSubArray(self, nums):
#         maxc=nums[0]
#         tmax=nums[0]
#         for x in range(1,len(nums)):
#             maxc=max(nums[x],nums[x]+maxc)
#             tmax=max(maxc,tmax)
#         return tmax


# ---------------------------------------------------------------------------------------------------------
## Sliding Window

import sys

class Solution:	   
    def maxSubArray(self, nums):
        self.nums = nums
        window_start = 0
        window_sum = 0 
        maximum = float('-inf')
        # maximum = -sys.maxsize - 1

        for window_end in range(len(nums)):
            window_sum += nums[window_end]
            maximum = max(maximum, window_sum)

            while window_sum < 0:
                window_sum -= nums[window_start]
                window_start += 1

        return maximum

arr = [-2,1,-3,4,-1,2]
classObject = Solution()
print("Original Array", arr)
print("The contiguous subarray (containing at least one number) which has the largest sum and return its sum ", classObject.maxSubArray(arr))

#Time Complexity : O(n)    
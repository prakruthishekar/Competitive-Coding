# Given an integer array nums, find a contiguous non-empty subarray within the array that 
# has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.



# class Solution(object):
#     def maxProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         #  Initialize max product,min product and answer
#         ans = nums[0]
#         max_prod = 1
#         min_prod = 1

#         for i in range(len(nums)):
#             #  if number is negative, we will swap max prod and min prod
#             if(nums[i]<0):

#                 max_prod = max_prod + min_prod
#                 min_prod = max_prod - min_prod
#                 max_prod = max_prod - min_prod
#             # find current max prod each time    
#             max_prod = max(nums[i],max_prod*nums[i]) 
#             # find current min prod each time
#             min_prod = min(nums[i],min_prod*nums[i])
#             # store the maximum product each time
#             ans = max(ans,max_prod)
        
#         return ans
    



class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maximum = float('-inf')
        window_sum = 1
        for window_end in range(len(nums)):
            window_sum *= nums[window_end]
            maximum = max(maximum, window_sum)
            if( nums[window_end] == 0):
                window_sum = 1
        
        window_sum = 1
        for window_end in range(len(nums)-1, 0, -1):
            window_sum *= nums[window_end]
            maximum = max(maximum, window_sum)
            if( nums[window_end] == 0):
                window_sum = 1

        return maximum

     

nums = [2,3,-2,-2,30,35,4,-4,4]
nums1 = [-2,0,-1]
classObject = Solution() 
print(classObject.maxProduct(nums))    
print(classObject.maxProduct(nums1))         

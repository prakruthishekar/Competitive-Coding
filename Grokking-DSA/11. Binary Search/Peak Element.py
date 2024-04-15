# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, 
# and return its index. If the array contains multiple peaks, 
# return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, 
# an element is always considered to be strictly greater than a neighbor 
# that is outside the array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where 
# the peak element is 2, or index number 5 where the peak element is 6.



def findPeakElement(nums) -> int:
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1
        
        left = 1
        right = len(nums)-1
        while left < right:
            m = (left + right)//2
            if nums[m-1]<nums[m]>nums[m+1]:
                return m
            elif nums[m-1]<nums[m]<nums[m+1]:
                left = m + 1
            else:
                right = m
            
        return left

print(findPeakElement([1,2,1,3,4]))
print(findPeakElement([1,2,3,1]))

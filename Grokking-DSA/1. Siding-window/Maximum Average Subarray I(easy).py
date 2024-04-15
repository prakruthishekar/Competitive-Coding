# You are given an integer array nums consisting of n elements, 
# and an integer k.

# Find a contiguous subarray whose length is equal to k that has 
# the maximum average value and return this value. Any answer with a 
# calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000

def findMaxAverage(nums, k: int):
        iterator = 0
        windowSum = 0
        maxSum = float('-inf')
        for i in range(len(nums)):
            windowSum += nums[i] # add next element
#slide window, we don't need to slide if we'hv not hit the required size of k
            if(i >= k-1):
                maxSum = max(windowSum/k,maxSum)
                windowSum -= nums[iterator]
                iterator += 1    
        return maxSum


print(findMaxAverage([1,12,-5,-6,50,3], 4))
print(findMaxAverage([-1], 1))

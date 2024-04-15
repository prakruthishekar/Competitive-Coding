# Given an array of integers nums and an integer k, return the total 
# number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

#how to run start
#subarraySum([1,1,1], 2)
#how to run end

def subarraySum(nums, k):
    
#first we start from a sum which is equal to 0, and the count of it is 1. 
# this is the input list ex :   [1 4 9 -5 8]
# this is the sum array (s) ex : [0  1    5    13    8    16 ]    
    
    sumDict = {0:1}
    n = len(nums)
    count = 0 
    s = 0 
    
    for num in nums:       
        s += num
#we make sure to check if the sum - k is already in the dictionary, if so, increase the count.         
        if s-k in sumDict:
            count += sumDict[s-k]
#we check if s is already in the sumDict, if so, increase by 1, if not assign 1.             
        if s in sumDict:
            sumDict[s] +=1
        else:
            sumDict[s] = 1
 
    return count



# def subarraySum(nums, k: int) -> int:
#     if len(nums) == 1:
#         return 1 if nums[0] == k else 0

#     count = 0
#     window_start = 0
#     window_sum = 0

#     for window_end in range(len(nums)):
#         window_sum += nums[window_end]

#         while window_sum > k:
#             window_sum -= nums[window_start]
#             window_start += 1

#         if window_sum == k:
#             count += 1

#     return count



print(subarraySum(nums = [-1,-1,1], k = 0))
print(subarraySum(nums = [1,2,3], k = 3))

# Given an array nums containing n distinct numbers in the range [0, n], return the 
# only number in the range that is missing from the array.

 

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
# 2 is the missing number in the range since it does not appear in nums.


##  Using HashMAp

# class Solution:
#     def missingNumber(self, nums) -> int:
        # seen = {}
        # for num in nums:
        #     seen[num] = True
            
        # for i in range(0, len(nums) + 1):
        #     if i not in seen:
        #         return i


# # UsingSummation Notation:

# class Solution:
#     def missingNumber(self, nums) -> int:
#         return (len(nums)*len(nums) + len(nums)) // 2 - sum(nums)


# Predict what the sum should be (n being the length of the array)
# Subtract it by all the numbers in the array
# Example:
# [3, 0, 2] Length = 3
# Prediction: 3+2+1 = 6
# SumOfArray: 3+0+2=5
# MissingNum: Pre-Sum = 6 - 5 = 1


## Bitwise    
# While finding the sum of numbers from 1 to nn, we can get 
# integer overflow when nn is large so better to go with Bitwise
class Solution:
    def missingNumber(self, nums) -> int:
        
        result = 0
        
        for counter,value in enumerate(nums):
            
            result ^= counter+1 # XOR result with numbers from the complete series
            result ^= value # XOR with the numbers given in num series
            
        return result


# Intution:

# XOR is a bitwise operation.
# The output is true when two values are not the same (exclusive) E.g 1^0 = 1 , 
# 1^1 =0 , 2^0 = 2 , 2^2 = 0.
# Value that is XOR with itself is 0
# With XOR, you can rearrange the numbers to get the following pattern

# 1^1 = 0
# 1^0 = 1

# 1^1 = 0
# 0^1 = 1

# For the fun part, XOR operations are commutative :

# 1^1^2 == (1^1)^2 == (2^1)^1 == 2

# Order does not mater when you use XOR, if there are two instances of the same number, 
# the XOR operations cancel each other out to get 0

# result = 3
# result ^= 5
# result ^= 6
# result ^= 3
# result ^= 6
# result ^= 5
# The result variable is 0 as 3^5^6^3^6^5 == (3^3) ^ (5^5) ^ (6^6) == 0


classObject = Solution()

print("the missing number in the range: ", classObject.missingNumber([3,0,1]))
print("the missing number in the range: ", classObject.missingNumber([9,6,4,2,3,5,7,0,1]))

#Time Complexity : O(n)           
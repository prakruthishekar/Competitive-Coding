# Given an unsorted array containing numbers, find the smallest 
# missing positive number in it.

# Example 1:

# Input: [-3, 1, 5, 4, 2]
# Output: 3
# Explanation: The smallest missing positive number is '3'


# Input: [3, -2, 0, 1, 2]
# Output: 4


# Input: [3, 2, 5, 1]
# Output: 4




# Solution 
# place the numbers on their correct indices and ignore all numbers that are 
# out of the range of the array (i.e., all negative numbers and all numbers 
# greater than or equal to the length of the array). Once we are done 
# with the cyclic sort we will iterate the array and the first index that 
# does not have the correct number will be the smallest missing positive number!

def first_missing_positive(nums):
    i = 0
    while( i < len(nums)):
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] < len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i+= 1
    
    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    return len(nums)+1

print(first_missing_positive([-3, 1, 5, 4, 2]))
print(first_missing_positive([3, -2, 0, 1, 2]))
print(first_missing_positive([3, 2, 5, 1]))
print(first_missing_positive([1,1]))







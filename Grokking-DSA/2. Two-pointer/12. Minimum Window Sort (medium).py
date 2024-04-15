# Minimum Window Sort (medium) #
# Given an array, find the length of the smallest subarray in it which 
# when sorted will sort the whole array.

# Example 1:

# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] 
# to make the whole array sorted
# Example 2:

# Input: [1, 3, 2, 0, -1, 7, 10]
# Output: 5
# Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] 
# to make the whole array sorted
# Example 3:

# Input: [1, 2, 3]
# Output: 0
# Explanation: The array is already sorted




from ast import List


def findUnsortedSubarray(nums):
    if len(nums) == 1:
        return 0
    
    max_val = float('-inf')
    min_val = float('inf')
    left_idx = -1
    right_idx = -1
    
    # Find the rightmost index that violates Rule 1
    for i in range(len(nums)):
        max_val = max(max_val, nums[i])
        if nums[i] < max_val:
            right_idx = i
    
    # Find the leftmost index that violates Rule 2
    for i in range(len(nums) - 1, -1, -1):
        min_val = min(min_val, nums[i])
        if nums[i] > min_val:
            left_idx = i
    
    # Return the difference
    if left_idx == right_idx:
        return 0
    return right_idx - left_idx + 1



print(findUnsortedSubarray([1, 3, 2, 0, -1, 7, 10]))
print(findUnsortedSubarray([1, 2, 5, 3, 7, 10, 9, 12]))



# Time complexity #
# The time complexity of the above algorithm will be 
# O(N).

# Space complexity #
# The algorithm runs in constant space 
# O(1)
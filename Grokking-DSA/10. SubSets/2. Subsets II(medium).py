# Given an integer array nums that may contain duplicates, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]


def subsets(nums):
    nums.sort()

    subsets = [[]]
    start = 0
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            start = 0
        size = len(subsets)
        for j in range(start, size):
            subset = list(subsets[j])
            subset.append(nums[i])
            subsets.append(subset)
        start = size

    return subsets


print(subsets([1,2,2]))
print(subsets([0]))

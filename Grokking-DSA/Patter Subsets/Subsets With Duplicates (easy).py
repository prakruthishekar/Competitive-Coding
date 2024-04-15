# Problem Statement #
# Given a set of numbers that might contain duplicates, find all of its distinct subsets.

# Example 1:

# Input: [1, 3, 3]
# Output: [], [1], [3], [1,3], [3,3], [1,3,3]
# Example 2:

# Input: [1, 5, 3, 3]
# Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 




                # Solution

# Given set: [1, 5, 3, 3]  
# Sorted set: [1, 3, 3, 5]

# Start with an empty set: [[]]
# Add the first number (1) to all the existing subsets to create new subsets: [[], [1]];
# Add the second number (3) to all the existing subsets: [[], [1], [3], [1,3]].
# The next number (3) is a duplicate. If we add it to all existing subsets we will get:
#     [[], [1], [3], [1,3], [3], [1,3], [3,3], [1,3,3]]
# We got two duplicate subsets: [3], [1,3]  
# Whereas we only needed the new subsets: [3,3], [1,3,3]  
# To handle this instead of adding (3) to all the existing subsets, we only add it to the new subsets which were created in the previous (3rd) step:

#     [[], [1], [3], [1,3], [3,3], [1,3,3]]
# Finally, add the forth number (5) to all the existing subsets: [[], [1], [3], [1,3], [3,3], [1,3,3], [5], [1,5], [3,5], [1,3,5], [3,3,5], [1,3,3,5]]





def find_subsets(nums):
    nums.sort()
    subsets = []
    subsets.append([])
    startIndex, endIndex = 0, 0
    for i in range(len(nums)):
        startIndex = 0
        if i > 0 and nums[i] == nums[i-1]:
            startIndex = endIndex + 1
        endIndex = len(subsets) - 1
        for j in range(startIndex, endIndex + 1):
            set = list(subsets[j])
            set.append(nums[i])
            subsets.append(set)

    return subsets

print(find_subsets([1,5,3,3]))
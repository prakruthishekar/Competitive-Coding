
# Problem Statement #
# Given a set with distinct elements, find all of its distinct subsets.

# Example 1:

# Input: [1, 3]
# Output: [], [1], [3], [1,3]
# Example 2:

# Input: [1, 5, 3]
# Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]




                                #Solution

# Given set: [1, 5, 3]

# Start with an empty set: [[]]
# Add the first number (1) to all the existing subsets to create new subsets: [[], [1]];
# Add the second number (5) to all the existing subsets: [[], [1], [5], [1,5]];
# Add the third number (3) to all the existing subsets: [[], [1], [5], [1,5], [3], [1,3], [5,3], [1,5,3]].





def find_subsets(nums):
    subsets = []
    subsets.append([])
    for currentNumber in nums:
        n = len(subsets)
        for i in range(n):
            set = list(subsets[i])
            set.append(currentNumber)
            subsets.append(set)

    return subsets

print(find_subsets([1,5,3]))




# Time complexity #
# Since, in each step, the number of subsets could double (if not duplicate) as we add 
# each element to all the existing subsets, the time complexity of the above algorithm is 
# O(2^N) where ‘N’ is the total number of elements in the input set. 
# This also means that, in the end, we will have a total of O(2^N) subsets at the most.

# Space complexity #
# All the additional space used by our algorithm is for the output list. 
# Since at most we will have a total of O(2^N) subsets, the space complexity of our 
# algorithm is also O(2^N)

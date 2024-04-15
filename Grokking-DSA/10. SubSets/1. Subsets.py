# Given a set with distinct elements, find all of its distinct subsets.

# Example 1:

# Input: [1, 3]
# Output: [], [1], [3], [1,3]
# Example 2:

# Input: [1, 5, 3]
# Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]


# *************************************************************************************

# Solution
# Given set: [1, 5, 3]

# Start with an empty set: [[]]
# Add the first number (1) to all the existing subsets to create new subsets: [[], [1]];
# Add the second number (5) to all the existing subsets: [[], [1], [5], [1,5]];
# Add the third number (3) to all the existing subsets: [[], [1], [5], [1,5], [3], [1,3], [5,3], [1,5,3]].


def subsets(nums):
    subsets = []
    subsets.append([])
    for currentNumber in nums:
        # we will take the existing subsets and insert the current number 
        # in them to create new subsets
        n = len(subsets)

        for i in range(n):
            # create a new subset from the existing subset and insert
            #  the current element to it
            set = list(subsets[i])
            set.append(currentNumber)
            subsets.append(set)

    return subsets




# Using backtracking

def subsets(nums):
    def backtrack(start, end, tmp):
        ans.append(tmp[:])
        for i in range(start, end):
            tmp.append(nums[i])
            backtrack(i+1, end, tmp)
            tmp.pop()
    ans = []
    backtrack(0, len(nums), [])
    return ans

print(subsets([1,3,5]))
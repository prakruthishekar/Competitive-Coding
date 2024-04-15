# Given an integer array nums of length n where all the integers of 
# nums are in the range [1, n] and each integer appears once or twice, 
# return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only 
# constant extra space.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []


# def findDuplicates(N):
#         S, A = set(), []
#         for n in N:
#             if n in S: 
#                 A.append(n)
#             else: 
#                 S.add(n)
#         return A


# O(n) time complexity with O(1) constant space
def findDuplicates(N):
        A = []
        for n in N:
            if N[abs(n)-1] > 0: 
                N[abs(n)-1] = -N[abs(n)-1]
            else: A.append(abs(n))
        return A


print(findDuplicates([4,3,2,7,8,2,3,1]))        

# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
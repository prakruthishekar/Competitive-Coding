# Given two version numbers, version1 and version2, compare them.

# Version numbers consist of one or more revisions joined by a dot '.'. 
# Each revision consists of digits and may contain leading zeros. Every 
# revision contains at least one character. Revisions are 0-indexed from 
# left to right, with the leftmost revision being revision 0, the next 
# revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

# To compare version numbers, compare their revisions in left-to-right order.
# Revisions are compared using their integer value ignoring any leading zeros. 
# This means that revisions 1 and 001 are considered equal. If a version number
# does not specify a revision at an index, then treat the revision as 0. For example, 
# version 1.0 is less than version 1.1 because their revision 0s are the same, but their
# revision 1s are 0 and 1 respectively, and 0 < 1.

# Return the following:

# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.
 

# Example 1:

# Input: version1 = "1.01", version2 = "1.001"
# Output: 0
# Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
# Example 2:

# Input: version1 = "1.0", version2 = "1.0.0"
# Output: 0
# Explanation: version1 does not specify revision 2, which means it is treated as "0".
# Example 3:

# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
# Explanation: version1's revision 0 is "0", while version2's revision 0 is "1".
# 0 < 1, so version1 < version2.








# def compareVersion(version1: str, version2: str) -> int: 
#         v1 = version1.split('.')
#         v2 = version2.split('.')
#         # Get the maximum length between the two lists
#         n = max(len(v1), len(v2))
#         # Iterate over the revisions of both lists
#         for i in range(n):
#             # Convert each revision to an integer if it exists, otherwise use 0
#             r1 = int(v1[i]) if i < len(v1) else 0
#             r2 = int(v2[i]) if i < len(v2) else 0
#             # Compare revisions and return result if different
#             if r1 < r2:
#                 return -1
#             elif r1 > r2:
#                 return 1
#         # Return 0 if all revisions are equal
#         return 0



#BestApproach
# Two pointers

def compareVersion(version1: str, version2: str) -> int: 
        
        first = second = 0

        while first < len(version1) or second < len(version2):
            num1 = num2 = 0
            while first < len(version1) and version1[first] != '.':
                num1 = num1 * 10 + int(version1[first])
                first +=1
            while second < len(version2) and version2[second] != '.':
                num2 = num2 * 10 + int(version2[second])
                second += 1
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1

            first +=1 
            second +=1
            
        return(0)


print(compareVersion("1.01", "1.001"))
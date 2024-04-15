# Given a string s, find the first non-repeating character in it and 
# return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1


import collections


def firstUniqChar(s):
        hset = collections.Counter(s);
        # Traverse the string from the beginning...
        for idx in range(len(s)):
            # If the count is equal to 1, it is the first distinct character in the list.
            if hset[s[idx]] == 1:
                return idx
        return -1       # If no character appeared exactly once...


print(firstUniqChar("loveleetcode"))
print(firstUniqChar("leetcode"))


# Complexity Analysis

# Time complexity: O(N)since we go through the string of length N two times.
# Space complexity: O(1) because English alphabet contains 26 letters.

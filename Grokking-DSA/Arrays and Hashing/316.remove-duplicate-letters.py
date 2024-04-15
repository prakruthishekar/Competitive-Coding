#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        stack = []
        for i in s:
            if i in stack:
                continue
            else:
                stack.append(i)
        return stack.sort()
        
# @lc code=end


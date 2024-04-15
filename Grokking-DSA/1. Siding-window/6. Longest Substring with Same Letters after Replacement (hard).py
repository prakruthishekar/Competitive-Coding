# Problem Statement #
# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter,
# find the length of the longest substring having the same letters after replacement.

# Example 1:

# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
# Example 2:

# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
# Example 3:

# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        counter = defaultdict(lambda : 0)
        left = 0
        max_frequency = float('-infinity')
        max_window = 0
        
        for right in range(len(s)):
            
            counter[s[right]] += 1
            current_window = right - left + 1
            if counter[s[right]] > max_frequency:
                max_frequency = counter[s[right]]
            
            while current_window - max_frequency > k:
                counter[s[left]] -= 1
                current_window -= 1
                left += 1
				
            if max_window < current_window:
                max_window = current_window
        
        return max_window

    # def characterReplacement(self, s: str, k: int) -> int:
    #     count = {}
    #     left_p = 0
    #     res = 0
    #     max_freq = 0
    #     for right_p in range(len(s)):
    #         # print(count.get(s[right_p], 0))
    #         # a = count.get(s[right_p], 0)
    #         count[s[right_p]] = 1 + count.get(s[right_p], 0)
    #         max_freq = max(max_freq, count[s[right_p]])
    #         if (right_p - left_p + 1) - max_freq > k:
    #             count[s[left_p]] -= 1
    #             left_p += 1
    #         res = max(res, right_p - left_p + 1)
    #     return res

classObject = Solution()
print("The longest substring without any repeating characters is aabzccbb k = 2 is " ,classObject. characterReplacement("aabzccbb",2))
print("The longest substring without any repeating characters is abbbb k = 3 is " , classObject.characterReplacement("abbbb",3))
print("The longest substring without any repeating characters is abccde k = 1 is " , classObject.characterReplacement("abccde",1))
# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"



def longestPalindrome(s: str) -> str:
    n = len(s)
    # Create a table to store the results of subproblems
    dp = [[False] * n for _ in range(n)]

    # All substrings of length 1 are palindromes
    max_len = 1
    start = 0
    for i in range(n):
        dp[i][i] = True

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_len = 2
            start = i

    # Check for substrings of length greater than 2
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if k > max_len:
                    max_len = k
                    start = i

    return s[start:start + max_len]


print(longestPalindrome("babad"))


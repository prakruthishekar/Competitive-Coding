# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false


def wordBreak(s: str, wordDict) -> bool:
    n = len(s)
    # Create a set for efficient word lookup
    wordSet = set(wordDict)
    # Create a dynamic programming table to store the subproblem results
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            # Check if the substring s[j:i] is in the wordSet and dp[j] is True
            if s[j:i] in wordSet and dp[j]:
                dp[i] = True
                break

    return dp[n]
        
print(wordBreak("leetcode",["leet","code"]))
print(wordBreak("applepenapple",["apple","pen"]))
print(wordBreak("catsandog",["cats","dog","sand","and","cat"]))



# Let n be the length of the input string s.
# The function uses two nested loops to iterate over all possible substrings of s.
# The outer loop runs n times, and the inner loop runs from 0 to i-1, where i is the current iteration of the outer loop.
# Therefore, the total number of iterations for the nested loops is roughly (n * (n+1)) / 2, which is proportional to n^2.
# Inside the inner loop, the function checks if each substring s[j:i] is in the wordSet and if dp[j] is True.
# The substring lookup in the wordSet and the dp array access both have constant time complexity.
# Thus, the overall time complexity of the function is approximately O(n^2).



# The space complexity of the wordBreak function is as follows:

# The function uses a dynamic programming table dp of size n + 1 to store the subproblem results.
# Additionally, it creates a wordSet set to efficiently check word existence.
# The space complexity is dominated by the dp table and the wordSet.
# Both the dp table and the wordSet have a space complexity of O(n) since they store at most n + 1 elements.
# Therefore, the overall space complexity of the function is O(n).
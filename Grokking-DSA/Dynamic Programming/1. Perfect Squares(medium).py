# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words,
# it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect 
# squares while 3 and 11 are not.

 

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
1, 4, 9, 16
2, 3
# from cmath import sqrt

from math import sqrt


def numSquares(n: int) -> int:
        dp = [float("inf")]*(n+1)
        for i in range(len(dp)):
            if int(sqrt(i)) == sqrt(i):
                dp[i] = 1
            else:
                for j in range(int(sqrt(i))+1):
                    dp[i] = min(dp[i], dp[i-j*j]+1)
        print("Ans")
        return dp[-1]


print(numSquares(n = 3))
print(numSquares(n = 13))

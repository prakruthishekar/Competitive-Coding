# Given an m x n binary matrix filled with 0's and 1's, find the largest square 
# containing only 1's and return its area.


# Input: matrix = [["1","0","1","0","0"],
#                  ["1","0","1","1","1"],
#                  ["1","1","1","1","1"],
#                  ["1","0","0","1","0"]]

# Output: 4
# Example 2:


# Input: matrix = [["0","1"],
#                  ["1","0"]]
# Output: 1
# Example 3:

# Input: matrix = [["0"]]
# Output: 0


def maximalSquare(matrix) -> int:
        # Get the dimensions of the matrix
        m, n = len(matrix), len(matrix[0])
        
        # Initialize the dp array
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the max size of the square seen so far
        max_size = 0
        
        # Fill the dp array
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        # First row or column, so the maximum size of the square is 1
                        dp[i][j] = 1
                    else:
                        # Check the values of the cells to the left, top, and top-left of the current cell
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                    # Update the max size of the square seen so far
                    max_size = max(max_size, dp[i][j])
        
        # Return the area of the largest square
        return max_size * max_size

print(maximalSquare([["1","0","1","0","0"],
                     ["1","0","1","1","1"],
                     ["1","1","1","1","1"],
                     ["1","0","0","1","0"]]))
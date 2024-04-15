# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
# word = "ABCCED"
# Output: true

def exist(board, word: str) -> bool:
        def dfs(i: int, j: int, k: int) -> bool:
            if k == len(word):
                return True
            # print(board[i][j])
            # print(word[k])
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
# To mark the current cell as visited, it temporarily changes the character at (i, j) to '/'
            temp, board[i][j] = board[i][j], '/'
            res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            board[i][j] = temp
            return res
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))




# The time complexity of the exist function can be analyzed as follows:

# Let m be the number of rows in the board and n be the number of columns.
# The function iterates over each cell in the board using two nested loops, resulting in a total of m * n iterations.
# For each cell, the dfs function is called, which performs a recursive depth-first search.
# In the worst case, each call to dfs explores up to four adjacent cells (up, down, left, right).
# The depth of the recursion is at most the length of the word, k.
# Therefore, the worst-case time complexity of the dfs function is O(4^k) since there are four possible directions to explore at each recursive call.
# Since the dfs function is called for each cell in the board, the overall time complexity of the exist function is O(m * n * 4^k).


# Regarding space complexity:

# The space complexity is determined by the depth of the recursion in the dfs function.
# At any given moment, the maximum depth of the recursion is the length of the word, k.
# Additionally, the space complexity is influenced by the temporary changes made to the board by replacing characters with '/'.
# Overall, the space complexity is O(k) due to the recursion depth and the auxiliary space used within the dfs function.
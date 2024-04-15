# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle).
# You can move up, down, left, or right from and to an empty cell in one step.

# Return the minimum number of steps to walk from the upper left corner 
# (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles.
# If it is not possible to find such walk return -1.

 

# Example 1:


# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6
# Explanation: 
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6.
#  Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
# Example 2:


# Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# Output: -1
# Explanation: We need to eliminate at least two obstacles to find such a walk.


import collections


def shortestPath(grid, k: int) -> int:
    rows = len(grid)
    cols = len(grid[0])

    target = (rows - 1,cols - 1)

    if k >= (rows - 1) + (cols - 1):
        return rows + cols - 2

#(total number of steps taken), (represent current state of teh path i.e currentRow, currentCol, totalObstacle elemination)
    queue = collections.deque([(0, (0, 0, k))])
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    seen= set([(0, 0, k)])

    while queue:
        steps, (row, col, removals_left) = queue.popleft()

        if (row, col) == target:
            return steps
        
        for row_inc, col_inc in directions:
            new_row = row + row_inc
            new_col = col + col_inc

            if (0 <= new_row < rows) and (0 <= new_col < cols):
                new_removals = removals_left - grid[new_row][new_col]
                new_state = (new_row, new_col, new_removals)

                if new_removals >= 0 and new_state not in seen:
                    seen.add(new_state)
                    queue.append((steps + 1, new_state))
    
    return -1


print(shortestPath(grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1))
print(shortestPath(grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1))

# Time Compexity : O(N) * K = O(N*K)
# S: O(N * K) = O(NK)

# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/
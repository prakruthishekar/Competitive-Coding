# Given an m x n integer matrix matrix, if an element is 0, 
# set its entire row and column to 0's.

# You must do it in place.

 

# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]


def setZeroes(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    if not matrix:
        return []

    m = len(matrix)
    n = len(matrix[0])
    zeroes_row = [False] * m
    zeroes_col = [False] * n
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                zeroes_row[row] = True
                zeroes_col[col] = True

    for row in range(m):
        for col in range(n):
            if zeroes_row[row] or zeroes_col[col]:
                matrix[row][col] = 0

    return matrix

# def setZeroes(matrix) -> None:
#     row = set()
#     column = set()
    
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == 0:
#                 row.add(i)
#                 column.add(j)          
#     for i in row:
#         for j in range(len(matrix[0])):
#             matrix[i][j] = 0
#     for i in column:
#         for j in range(len(matrix)):
#             matrix[j][i] = 0 

#     return matrix         

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))                             
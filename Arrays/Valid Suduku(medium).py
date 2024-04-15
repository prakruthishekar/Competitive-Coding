from collections import defaultdict
# def isValidSudoku(board) -> bool:
#         rows = defaultdict(set)
#         cols = defaultdict(set)
#         grids = defaultdict(set)        
#         for r in range(9):
#             for c in range(9):
#                 if board[r][c]==".":
#                     continue
#                 if (board[r][c] in rows[r] or board[r][c] in cols[c] 
#                 or board[r][c] in grids[(r//3,c//3)]):
#                     return False

#                 rows[r].add(board[r][c])
#                 cols[c].add(board[r][c])
#                 grids[(r//3,c//3)].add(board[r][c])                                                                       
                
#         return True


def isValidSudoku(board) -> bool:        
        seen = set()
        for i in range(9):
            for j in range(9):
                number = str(board[i][j])
                if number != '.':
                    row = number +'in row' + str(i)
                    col = number +'in col' + str(j)
                    # // for integer
                    block = number +'in block' + str(i//3) + str(j//3)
                    if row in seen or col in seen or block in seen:
                        return False
                    seen.add(row)
                    seen.add(col)
                    seen.add(block)
        return True


print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]
                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]
                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9",".",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]]))
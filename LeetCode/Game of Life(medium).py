# The board is made up of an m x n grid of cells, 
# where each cell has an initial state: live (represented by a 1)
# or dead (represented by a 0). Each cell interacts with its eight
# neighbors (horizontal, vertical, diagonal) using the following four
# rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies 
# as if caused by under-population.

# Any live cell with two or three live neighbors lives on to the next generation.

# Any live cell with more than three live neighbors dies, as if by over-population.

# Any dead cell with exactly three live neighbors becomes a live cell, 
# as if by reproduction.

# The next state is created by applying the above rules simultaneously 
# to every cell in the current state, where births and deaths occur simultaneously. 
# Given the current state of the m x n grid board, return the next state.




def gameOfLife(board) -> None:
        r = len(board) ; 
        c = len(board[0])

        for i in range(r):
            for j in range(c):  
                live = 0
                dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    
# Go in all 8 directions and keep count of live cells
                for d in dirs:
                    x = i + d[0] 
                    y = j + d[1]
                    print(board[x][y])
                    if x>=0 and y>=0 and x<r and y<c and board[x][y] in [1, 3]:
                        live += 1
# If board[x][y] is equal to 1, it means the neighboring cell at (x, y) 
# is currently alive. Therefore, it contributes to the count of live 
# neighbors (live += 1).

# If board[x][y] is equal to 3, it means the neighboring cell at (x, y) 
# is currently alive but is going to die in the next generation based 
# on the Game of Life rules. In this case, it also contributes to the 
# count of live neighbors (live += 1) because it's considered alive
#  in the current generation.              
                if board[i][j] == 0 and live == 3:
                    board[i][j] = 2
                   
                elif board[i][j] == 1 and live != 2 and live != 3:
                    board[i][j] = 3
           
        for i in range(r):
            for j in range(c):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0


print(gameOfLife([[0,1,0],
                  [0,0,1],
                  [1,1,1],
                  [0,0,0]]))
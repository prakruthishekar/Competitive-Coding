# On an alphabet board, we start at position (0, 0), corresponding to 
# character board[0][0].

# Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as 
# shown in the diagram below.



# We may make the following moves:

# 'U' moves our position up one row, if the position exists on the board;
# 'D' moves our position down one row, if the position exists on the board;
# 'L' moves our position left one column, if the position exists on the board;
# 'R' moves our position right one column, if the position exists on the board;
# '!' adds the character board[r][c] at our current position (r, c) to the answer.
# (Here, the only positions that exist on the board are positions with letters on them.)

# Return a sequence of moves that makes our answer equal to target in 
# the minimum number of moves.  You may return any path that does so.

 

# Example 1:

# Input: target = "leet"
# Output: "DDR!UURRR!!DDD!"
# Example 2:

# Input: target = "code"
# Output: "RR!DDRR!UUL!R!"

def alphabetBoardPath(target: str) -> str:

    # store the letters position by using the below code
    letters_map = {}
    for i in range(26):
        letter = chr(ord('a') + i)
        letters_map[letter] = (i // 5, i% 5)
    moves = []

    #position starts from 0,0 and compare it with the actual position of the letter
    i, j = 0, 0


    for letter in target:
        next_i , next_j = letters_map[letter]

    # edge case to resolve issue with 'z' as that row doesn't contain anythig but z
        if (i,j) == letters_map['z'] and letter != 'z':
            moves.append("U")
            i -= 1

        while j != next_j:
            if j < next_j:
                moves.append("R")
                j += 1
            else:
                moves.append("L")
                j -= 1

        while i != next_i:
            if i < next_i:
                i += 1
                moves.append("D")
            else:
                moves.append("U")
                i -= 1

        

        moves.append("!")
    return ''.join(moves)


print(alphabetBoardPath(target = "leet"))
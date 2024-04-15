# def print_chessboard(n):
#     for i in range(n):
#         for j in range(n):
#             if (i + j) % 2 == 0:
#                 print("W", end=" ")
#             else:
#                 print("B", end=" ")
#         print()  # move to the next line after each row

# def main():
#     # take input for size of the chessboard
#     inputNum = int(input().strip())
#     print_chessboard(inputNum)

# if __name__ == "__main__":
#     main()


def find_special_element(matrix):
    rows, cols = len(matrix), len(matrix[0])
    
    for i in range(rows):
            # Find the largest element in the row
            largest_in_row = max(matrix[i])
            
            for col_index in range(cols):
                # If we find an occurrence of the largest element, check its column
                if matrix[i][col_index] == largest_in_row:
                    # Check if it's the smallest in its column
                    smallest_in_col = True
                    for j in range(rows):
                        if matrix[j][col_index] < largest_in_row:
                            smallest_in_col = False
                            break

                    # If largest in row and smallest in column, return the element
                    if smallest_in_col:
                        return largest_in_row
    # If no such element is found
    return -1

def main():
    # Input rows and columns
    # matrix_row, matrix_col = map(int, input().split())
    
    # # Input the matrix
    # matrix = [list(map(int, input().split())) for _ in range(matrix_row)]
    matrix = [[1,2,5],
              [3,4,6]]
    matrix = [[1,2],
              [3,4]]

    # Print the result
    print(find_special_element(matrix))

if __name__ == "__main__":
    main()

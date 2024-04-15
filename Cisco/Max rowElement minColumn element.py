def funcMatrix(matrix):
	n = len(matrix)
	max_in_row = [max(row) for row in matrix]
	min_in_col = [min(matrix[i][j] for i in range(n)) for j in range(n)]
	for i in range(n):
		for j in range(n):
			if matrix[i][j] == max_in_row[i] and matrix[i][j] == min_in_col[j]:
				return matrix[i][j]
	return -1

print(funcMatrix([[1,2],[3,4]]))


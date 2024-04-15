def numIslands(grid, directions=4):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    numberOfIslands = 0

    if directions == 4:
        d_rows = [1, -1, 0, 0]
        d_cols = [0, 0, 1, -1]
    elif directions == 8:
        d_rows = [1, -1, 0, 0, 1, 1, -1, -1]
        d_cols = [0, 0, 1, -1, 1, -1, 1, -1]
    else:
        raise ValueError("Directions must be either 4 or 8")

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        for dr, dc in zip(d_rows, d_cols):
            dfs(r + dr, c + dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                numberOfIslands += 1
                dfs(r, c)

    return numberOfIslands

grid_diagonal = [
    ['1', '0', '0'],
    ['0', '1', '0'],
    ['0', '0', '1']
]
# print(numIslands(grid_diagonal, 4)) # 3
print(numIslands(grid_diagonal, 8)) # 1




# Single island
grid1 = [
    ['1', '1', '0', '0'],
    ['1', '1', '0', '0'],
    ['0', '0', '0', '0'],
    ['0', '0', '0', '0']
]
assert numIslands(grid1, 4) == 1

# Three separate islands
grid2 = [
    ['1', '0', '1', '0'],
    ['0', '1', '0', '1'],
    ['1', '0', '1', '0'],
    ['0', '1', '0', '1']
]
assert numIslands(grid2, 4) == 8


# No islands
grid3 = [
    ['0', '0', '0'],
    ['0', '0', '0'],
    ['0', '0', '0']
]
assert numIslands(grid3, 4) == 0


# Single island connected diagonally
grid4 = [
    ['1', '0', '1'],
    ['0', '1', '0'],
    ['1', '0', '1']
]
assert numIslands(grid4, 8) == 1

# Multiple islands
grid5 = [
    ['1', '0', '1', '0'],
    ['0', '1', '1', '1'],
    ['1', '1', '0', '1']
]
assert numIslands(grid5, 8) == 1

# Differentiating islands with diagonals
grid6 = [
    ['1', '0', '1'],
    ['1', '0', '1'],
    ['1', '1', '1']
]
assert numIslands(grid6, 8) == 1



# Edge Case 1: Empty grid
grid_empty = []
assert numIslands(grid_empty, 4) == 0

# Edge Case 2: All land
grid_all_land = [['1']*5]*5
assert numIslands(grid_all_land, 4) == 1

# Edge Case 3: All water
grid_all_water = [['0']*5]*5
assert numIslands(grid_all_water, 4) == 0

# Edge Case 4: Single cell land/water
grid_single_land = [['1']]
grid_single_water = [['0']]
assert numIslands(grid_single_land, 4) == 1
assert numIslands(grid_single_water, 4) == 0

# Edge Case 5: Long horizontal line of land
grid_long_line = [['0']*10]*5 + [['1']*10] + [['0']*10]*5
assert numIslands(grid_long_line, 4) == 1

# Edge Case 6: Large grid with small islands
grid_large = [['0', '1', '0', '1'] * 50] * 200
result = numIslands(grid_large, 4)
print(result) # This will print the result of the function
assert result == 100



# Edge Case 7: Diagonal line of land
grid_diagonal = [
    ['1', '0', '0'],
    ['0', '1', '0'],
    ['0', '0', '1']
]
# assert numIslands(grid_diagonal, 4) == 3
assert numIslands(grid_diagonal, 8) == 1




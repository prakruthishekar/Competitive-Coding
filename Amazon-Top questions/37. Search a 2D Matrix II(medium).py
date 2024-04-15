# Write an efficient algorithm that searches for a value target in
#     an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],
#                  [10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true


def searchMatrix(matrix, target: int) -> bool:
        for r in matrix:
            if r[0] <= target and r[-1] >= target:
                left, right = 0, len(r)-1
                while left <= right:
                    mid = (left + right)//2
                    if r[mid] > target:
                        right = mid - 1
                    elif r[mid] < target:
                        left = mid + 1
                    else:
                        return True
            else:
                continue
        return False



print(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],
                    [3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
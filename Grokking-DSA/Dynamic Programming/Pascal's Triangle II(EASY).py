# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]

def getRow(rowIndex: int):
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        prev = getRow(rowIndex - 1)

        cur = [1] + [prev[i] + prev[i+1] for i in range(len(prev) - 1)] + [1]

        return cur

print(getRow(3))        
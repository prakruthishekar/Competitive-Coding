# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers 
# directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


def generate(numRows: int):
        # l = [0] * numRows
        # for i in range(numRows):
        #     l[i] = [0]*(i+1)
        #     l[i][0] = 1
        #     l[i][i] = 1
        #     for j in range(1,i):
        #         l[i][j] = l[i-1][j-1]+l[i-1][j]
        # return l

        if numRows   == 0: return []
        elif numRows == 1: return [[1]]
        Tri = [[1]]
        for i in range(1,numRows):
            row = [1]
            for j in range(1,i):
                row.append(Tri[i-1][j-1] + Tri[i-1][j]) 
            row.append(1)
            Tri.append(row)
        return Tri



print(generate(5))            
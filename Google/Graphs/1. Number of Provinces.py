# There are n cities. Some of them are connected, while some are not.
# If city a is connected directly with city b, and city b is connected directly 
# with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and 
# no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if 
# the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:


# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:


# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3


def findCircleNum(isConnected) -> int:
        root = [i for i in range(len(isConnected))]
        rank = [1] * len(isConnected)
        totalProvinces = len(isConnected)
        def find(x):
            if x == root[x]:
                return x
        # Some ranks may become obsolete so they are not updated
            root[x] = find(root[x])
            return root[x]

        # The union function with union by rank
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX] += 1
        
        for i in range(len(isConnected)):
            for j in range (len(isConnected)):
                if isConnected[i][j] and find(i) != find(j):
                    totalProvinces -= 1
                    union(i, j)

        
        return totalProvinces


print(findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]]))
print(findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]]))

# https://leetcode.com/problems/number-of-provinces/description/
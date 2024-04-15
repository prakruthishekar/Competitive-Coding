# You have a graph of n nodes. You are given an integer n and 
# an array edges where edges[i] = [ai, bi] indicates that there is
# an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

 

# Example 1:


# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2
# Example 2:


# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1

def countComponents(n: int, edges) -> int:
        root = [i for i in range(n)]
        rank = [1] * n
        countComponents = n  # Initialize countComponents to n (assuming each node is initially a separate component)
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
                nonlocal countComponents  # Use nonlocal keyword to modify countComponents
                countComponents -= 1  # Decrement countComponents when merging components
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX] += 1
        
        for i, j in edges:
            if find(i) != find(j):
                union(i, j)

        
        return countComponents

print(countComponents(n = 5, edges = [[0,1],[1,2],[3,4]]))
print(countComponents(n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]))



# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
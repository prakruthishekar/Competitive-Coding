# Given edges and the integers n, source, and destination, return true if there is a 
# valid path from source to destination, or false otherwise.

 

# Example 1:


# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2
# Example 2:


# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.



# BFS
import collections
class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        # Store all edges in 'graph'.
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # Store all the nodes to be visited in 'queue'.
        seen = [False] * n
        seen[source] = True
        queue = collections.deque([source])
    
        while queue:
            curr_node = queue.popleft()
            if curr_node == destination:
                return True
            # For all the neighbors of the current node, if we haven't visit it before,
            # add it to 'queue' and mark it as visited.
            for next_node in graph[curr_node]:
                if not seen[next_node]:
                    seen[next_node] = True
                    queue.append(next_node)
        
        return False


# DFS Recursive
class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        seen = [False] * n
        
        def dfs(curr_node):
            if curr_node == destination:
                return True
            if not seen[curr_node]:
                seen[curr_node] = True
                for next_node in graph[curr_node]:
                    if dfs(next_node):
                        return True
            return False
            
        return dfs(source)
    


# DFS Iterative
class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        # Store all edges according to nodes in 'graph'.
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # Start from source node, add it to stack.
        seen = [False] * n
        seen[source] = True
        stack = [source]
        
        while stack:
            curr_node = stack.pop()
            # Add all unvisited neighbors of the current node to stack 
            # and mark them as visited.
            for next_node in graph[curr_node]:
                if next_node == destination:
                    return True
                if not seen[next_node]:
                    seen[next_node] = True
                    stack.append(next_node)
        
        return seen[destination]
    

class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                root_x, root_y = root_y, root_x
            # Modify the root of the smaller group as the root of the
            # larger group, also increment the size of the larger group.
            self.rank[root_y] += self.rank[root_x]
            self.root[root_x] = root_y


# Disjoint Set Union (DSU)
class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        uf = UnionFind(n)

        for a, b in edges:
            uf.union(a, b)

        return uf.find(source) == uf.find(destination)

# Test cases
solution = Solution()
print(solution.validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2))
print(solution.validPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5))

# https://leetcode.com/problems/find-if-path-exists-in-graph/description/
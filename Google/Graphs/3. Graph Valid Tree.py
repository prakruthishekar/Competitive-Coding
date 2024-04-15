# You have a graph of n nodes labeled from 0 to n - 1. You are given an 
# integer n and a list of edges where edges[i] = [ai, bi] indicates that there 
# is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false 
# otherwise.

 

# Example 1:


# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true
# Example 2:


# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false

# # Iterative Depth-First Search.
import collections


# def validTree(n: int, edges) -> bool:
    
#     if len(edges) != n - 1: return False
    
#     # Create an adjacency list.
#     adj_list = [[] for _ in range(n)]
#     for A, B in edges:
#         adj_list[A].append(B)
#         adj_list[B].append(A)
    
#     # We still need a seen set to prevent our code from infinite
#     # looping if there *is* cycles (and on the trivial cycles!)
#     seen = {0}
#     stack = [0]
    
#     while stack:
#         node = stack.pop()
#         for neighbour in adj_list[node]:
#             if neighbour in seen:
#                 continue
#             seen.add(neighbour)
#             stack.append(neighbour)
    
#     return len(seen) == n




def validTree(n: int, edges) -> bool:
    if len(edges) != n - 1: return False
    
    # Create an adjacency list.
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)
    
    # We still need a seen set to prevent our code from infinite
    # looping if there *is* cycles (and on the trivial cycles!)
    seen = set()

    def dfs(node):
        if node in seen: return
        seen.add(node)
        for neighbour in adj_list[node]:
            dfs(neighbour)

    dfs(0)
    return len(seen) == n




def validTree(n: int, edges) -> bool:
    if len(edges) != n - 1: return False
    
    # Create an adjacency list.
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)
    
    # We still need a seen set to prevent our code from infinite
    # looping if there *is* cycles (and on the trivial cycles!)
    seen = {0}
    queue = collections.deque([0])
    
    while queue:
        node = queue.popleft()
        for neighbour in adj_list[node]:
            if neighbour in seen:
                continue
            seen.add(neighbour)
            queue.append(neighbour)
    
    return len(seen) == n



# print(validTree( n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]))
print(validTree(n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]))
print(validTree(n = 5 , edges = [[0,1],[0,4],[1,4],[2,3]]))


# https://leetcode.com/problems/graph-valid-tree/description/
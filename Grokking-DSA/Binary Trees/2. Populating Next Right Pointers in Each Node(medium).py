# You are given a perfect binary tree where all leaves are on the same level, 
# and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. 
# If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

 

# Example 1:


# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), 
# your function should populate each next pointer to point to its next right node, just like in Figure B. 
# The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:

# Input: root = []
# Output: []



# BFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
      1 (1)
    2 (2)->    3(1)
 4(4) -> 5(3) -> 6(2) -> 7(1)

"""
        if root ==  None:
            return None
        q = deque([root])
        while q:  # [1] [3,4,5]
            size = len(q) # 1 2
            while size > 0: #  > 0
                node = q.popleft() # node =1,2,3
                if size > 1 :# 
                    node.next = q[0] #  2.next = 3
                size -= 1          # size =1
                
                if node.left:         
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
    


# DFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
      1 (1)
    2 (2)->    3(1)
 4(4) -> 5(3) -> 6(2) -> 7(1)

"""
        self.dfs(root)
        return root
    
    ## (1). left child -> right child
    ## (2). right child -> next.left child
    def dfs(self,root):
        if root == None or root.left == None:
            return
        root.left.next = root.right
        if root.next != None: 
            root.right.next = root.next.left
        self.dfs(root.left)
        self.dfs(root.right)
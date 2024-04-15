# Problem Statement #
# Given a binary tree, connect each node with its level order successor. 
# The last node of each level should point to a null node.

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None

    def print_all_level_order(self):
        current = self
        while current:
            print(str(current.val) + " " ,end="") 
            current = current.next


def connect_all_level_order(root):
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    previousNode = None

    while queue:
        currentNode = queue.popleft()
        # add the node to the current level
        if previousNode:
            previousNode.next = currentNode
        previousNode = currentNode

        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)    

          

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

connect_all_level_order(root)

root.print_all_level_order()
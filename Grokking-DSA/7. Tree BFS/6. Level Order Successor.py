# Problem Statement 
# Given a binary tree and a node, find the level order successor of the given node 
# in the tree. The level order successor is the node that appears right after the given 
# node in the level order traversal.


from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_successor(root,key):
    result = []
    if root is None:
        return result
    
    queue = []
    queue.append(root)
    while queue:
        currentNode = queue.pop(0)
        # add the node to the current level
        if currentNode.left:
            queue.append(currentNode.left)

        if currentNode.right:
            queue.append(currentNode.right) 

        if currentNode.val == key:

            break

    return queue[0].val if queue else None                     

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.right.right.left = TreeNode(5)

print(find_successor(root, 7))




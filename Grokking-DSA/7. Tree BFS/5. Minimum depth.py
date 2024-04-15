# Find the minimum depth of a binary tree. The minimum depth is the number of nodes 
# along the shortest path from the root node to the nearest leaf node.

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minimumDepth(root):
    if root is None:
        return 0
    
    queue = deque()
    queue.append(root)
    mindepth = 0
    while queue:
        levelSize = len(queue)
        mindepth += 1 
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # add the node to the current level
            if not currentNode.left and not currentNode.right:
                return mindepth

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
root.right.right.left = TreeNode(5)



print("Minimum Depth:" + str(minimumDepth(root)))
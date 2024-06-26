# Given a binary tree, populate an array to represent its level-by-level traversal in 
# reverse order, i.e., the lowest level comes first. You should populate the values of all
# nodes in each level from left to right in separate sub-arrays.

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reverseOrder(root):
    result = deque()
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # add the node to the current level
            currentLevel.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result.appendleft(currentLevel)
    return result            

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print("Level order traversal :" + str(reverseOrder(root)))
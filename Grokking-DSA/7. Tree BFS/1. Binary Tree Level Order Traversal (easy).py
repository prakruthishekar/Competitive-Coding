from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    result = []
    if root is None:
        return result
    
    queue = []
    queue.append(root)

    while queue:
        levelSize = len(queue)
        currentLevel = []   
        for _ in range(levelSize):
            currentNode = queue.pop(0)
            # add the node to the current level
            currentLevel.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)
        result.append(currentLevel)
    return result            

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print("Level order traversal :" + str(levelOrder(root)))
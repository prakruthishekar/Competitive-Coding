from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maximumDepth(root):
    if root is None:
        return 0
    
    queue = deque()
    queue.append(root)
    maxdepth = 0
    while queue:
        levelSize = len(queue)
        maxdepth += 1 
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # add the node to the current level
            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)  

    return maxdepth                     

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.right.right.left = TreeNode(5)



print("Level order traversal :" + str(maximumDepth(root)))
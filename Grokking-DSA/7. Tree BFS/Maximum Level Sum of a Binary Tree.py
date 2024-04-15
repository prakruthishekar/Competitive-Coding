from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelAverage(root):
    result = {}
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    level = 0
    while queue:
        level += 1
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
        result[level] = (sum(currentLevel))
    return max(result, key= result.get)            

root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)
# root.right.left = TreeNode(10)
# root.right.right = TreeNode(5)


print("Level order traversal :" + str(levelAverage(root)))
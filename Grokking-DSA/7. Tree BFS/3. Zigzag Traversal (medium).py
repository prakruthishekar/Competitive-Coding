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
        return []

    queue = []
    queue.append(root)
    flag = True
    while queue:
        levelSize = len(queue)
        currentlevel = []

        for i in range(levelSize):
            currentNode = queue.pop(0)
            currentlevel.append(currentNode.val)

            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)
        if flag:
            result.append(currentlevel)
        else:
            result.append(currentlevel[::-1])
        flag = not flag    
    return result            

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(20)
root.right.left.right = TreeNode(17)



print("Level order traversal :" + str(levelOrder(root)))




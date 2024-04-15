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

    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " " , end ="")
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next

            print()



def connect_level_order(root):
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        previousNode = None
        for _ in range(levelSize):
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
connect_level_order(root)

root.print_level_order()
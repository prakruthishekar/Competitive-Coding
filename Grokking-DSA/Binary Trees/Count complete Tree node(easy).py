# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, 
# is completely filled in a complete binary tree, and all nodes in the 
# last level are as far left as possible. It can have between 1 and 2h nodes 
# inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: 6
# Example 2:

# Input: root = []
# Output: 0
# Example 3:

# Input: root = [1]
# Output: 1
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

# This is O(n) operation
def countNodes(root) -> int:
    if root is None:
        return 0
    return ( 1 + countNodes(root.left) + countNodes(root.right) )


# Creating the tree
node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left = Node(6)
node.right.left.right = Node(6)


print(countNodes(node))






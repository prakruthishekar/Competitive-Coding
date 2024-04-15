# Given a binary tree, return an array containing 
# nodes in its right view. The right view of a binary tree is the set of 
# nodes visible when the tree is seen from the right side.



#SolutionL We can follow the same BFS approach. The only additional thing 
# we will be do is to append the last node of each level to the result array.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_right_view(root):
    result = []
    if root is None:
        return result
    
    queue = []
    queue.append(root)

    while queue:
        levelSize = len(queue)
        for i in range(levelSize):
            currentNode = queue.pop(0)
            # add the node to the current level
            if i == levelSize - 1:
                result.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)
    
    return result            

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.left.left.left = TreeNode(3)


print("Level order traversal :" + str(tree_right_view(root)))
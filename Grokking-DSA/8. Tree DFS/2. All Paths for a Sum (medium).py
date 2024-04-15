# Problem Statement #
# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such 
# that the sum of all the node values of each path equals ‘S’.



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None


def find_path(root, sum):
    allPaths = []
    find_all_paths_recursive(root, sum, [], allPaths)
    return allPaths


def find_all_paths_recursive(currentNode,sum, currentPath, allPaths):
    if currentNode is None:
        return 

    #add current node to path
    currentPath.append(currentNode.val)

    #if the current node is a leaf and it's value is equal to the sum, we'hv found the path
    if currentNode.val == sum and currentNode.left is None and currentNode.right is None:
        allPaths.append(list(currentPath))
        # print(currentPath)
    else:
    #traverse left sub-tree
        find_all_paths_recursive(currentNode.left, sum - currentNode.val,currentPath, allPaths)
    #traverse right sub-tree
        find_all_paths_recursive(currentNode.right, sum - currentNode.val, currentPath, allPaths)
    # remove the current node from the path to backtrack
    del currentPath[-1]

#        12
#       /  \
#      7    1
#     /    / \
#    4   10   5

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
sum = 23
print(find_path(root,23))


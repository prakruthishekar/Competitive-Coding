# Given a binary tree and a number ‘S’, find if the tree has a path from 
# root-to-leaf such that the sum of all the node values of that path equals ‘S’.



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None


def has_path(root,sum):
    if root is None:
        return False

    #if the current node is a leaf and it's value is equal to the sum, we'hv found the path
    if root.val == sum and root.left is None and root.right is None:
        return True 
    
    # recursively call to traverse the left and right sub-Tree
    # return true if any of those two recursive call return true
    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)
              

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print(has_path(root,23))
print(has_path(root,16))


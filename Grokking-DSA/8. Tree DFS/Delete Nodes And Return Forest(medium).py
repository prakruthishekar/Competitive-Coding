# Given the root of a binary tree, each node in the tree has a distinct value.

# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

# Return the roots of the trees in the remaining forest. You may return the result in any order.

 

# Example 1:


# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
# Example 2:

# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None

def delNodes(root, to_delete):
        
    def dfs(node, parent, side, to_delete):
        if node:
            if node.val in to_delete:
                if side == "R" and parent:
                    parent.right = None
                if side == "L" and parent:
                    parent.left = None
                if node.left and node.left.val not in to_delete:
                    res.append(node.left)
                if node.right and node.right.val not in to_delete:
                    res.append(node.right)
            dfs(node.left, node, "L", to_delete)
            dfs(node.right, node, "R", to_delete)
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
    to_delete = set(to_delete)
    if not root:
        return []
    res = [] if root.val in to_delete else [root]
    dfs(root, None, "R", to_delete)
    return res

#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

delNodes(root = root, to_delete = [3,5])
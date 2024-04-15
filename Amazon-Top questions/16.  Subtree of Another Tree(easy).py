# Given the roots of two binary trees root and subRoot, return true if there 
# is a subtree of root with the same structure and node values of subRoot and 
# false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree 
# and all of this node's descendants. The tree tree could also be considered 
# as a subtree of itself.

 

# Example 1:


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

                #     3               
                #    / \
                #   4   5                 4
                #  /  \                  / \
                # 1    2                1   2

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(s, t) -> bool:
    def isSameTree(p, q) -> bool:
        if p and q:
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        return p is q
    
    if not s : 
        return False
    if isSameTree(s, t): 
        return True
    return isSubtree(s.left, t) or isSubtree(s.right, t)


# First Tree
#      3
#     / \
#    4   5
#   / \   
#  1   2 

tree1 = TreeNode(3)
tree1.left = TreeNode(4)
tree1.right = TreeNode(5)
tree1.left.left = TreeNode(1)
tree1.left.right = TreeNode(2)



# Second Tree
#       4
#      / \
#     1   2
tree2 = TreeNode(4)
tree2.left = TreeNode(1)
tree2.right = TreeNode(2)



print(isSubtree(tree1, tree2))
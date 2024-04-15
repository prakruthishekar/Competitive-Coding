# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# Example 2:

# Input: root = [1]
# Output: ["1"]




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None


def binaryTreePath(root):
    ans = []
    def solve(root, s):
        s += str(root.val)
        if not root.right and not root.left:
            ans.append(s)
            return
        if root.right:
            solve(root.right, s+"->")
        if root.left:
            solve(root.left, s+"->")
    solve(root, "")
    return ans          


        #   1
        #  / \ 
        # 2   3
      #    \   
    #       5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
print(binaryTreePath(root))



# Approach

# To find all the root-to-leaf paths, we can use a depth-first search (DFS) algorithm. 
# We'll implement a recursive helper function solve() that takes two parameters: 
# the current node and the current path string. The solve() function will traverse
# the tree in a depth-first manner and append the root-to-leaf paths to the ans list.

# In the solve() function:

# Append the string representation of the current node's value to the path string
# (s += str(root.val)).

# Check if the current node is a leaf node (i.e., it has no left or right child). 
# If so, it means we have reached the end of a root-to-leaf path. In this case, append
# the current path string to the ans list and return.

# If the current node has a right child, recursively call solve() with the right
#  child and the updated path string (solve(root.right, s + "->")).

# If the current node has a left child, recursively call solve() with the left
#  child and the updated path string (solve(root.left, s + "->")).

# After defining the solve() function, we initialize an empty ans list. 
# Then, we call solve() with the root node and an empty path string (""). Finally, we return the ans list, which contains all the root-to-leaf paths.
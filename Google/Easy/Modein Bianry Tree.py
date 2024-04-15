# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) 
# (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [1,null,2,2]
# Output: [2]
# Example 2:

# Input: root = [0]
# Output: [0]


from collections import defaultdict
# Structure of a Binary Tree Node
class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def findMode(root):
        def dfs(node, counter):
            if not node:
                return
            
            counter[node.val] += 1
            dfs(node.left, counter)
            dfs(node.right, counter)
            
        counter = defaultdict(int)
        dfs(root, counter)
        max_freq = max(counter.values())
        
        ans = []
        for key in counter:
            if counter[key] == max_freq:
                ans.append(key)     
        return ans


#       1
#      / \
#     2   2
#    / \   \
#   4   2   6

# Driver code
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(2)
	root.left.left = Node(4)
	root.left.right = Node(2)
	root.right.right = Node(6)

	# Function call
	print("Inorder traversal of binary tree is:")
	print(findMode(root))
# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
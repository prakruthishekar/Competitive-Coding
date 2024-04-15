# The left subtree is traversed first
# Then the root node for that subtree is traversed
# Finally, the right subtree is traversed

# Structure of a Binary Tree Node
class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

# Function to print inorder traversal
def inorderTraversal(root):
        def helper(root, res):
            if root != None:
                helper(root.left, res)
                res.append(root.val)
                helper(root.right, res)
        res = []
        helper(root, res)
        return res

#       1
#      / \
#     2   3
#    / \   \
#   4   5   6

# Driver code
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.right = Node(6)

	# Function call
	print("Inorder traversal of binary tree is:")
	print(inorderTraversal(root))






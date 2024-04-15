# Given a binary tree where each node can only have a digit (0-9) value, 
# each root-to-leaf path will represent a number. Find the total sum of all the 
# numbers represented by all paths.

#  Example 1: 
#  Output: 408 Explaination: The sume of all path numbers: 17 + 192 + 199


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None


def find_sum_of_path_number(root):
    return find_root_to_leaf_pathNumbers(root, 0 )

def find_root_to_leaf_pathNumbers(currentNode,pathSum):
    if currentNode is None:
        return 0
    #Calculate the pathe of the current node
    pathSum = 10 * pathSum + (currentNode.val)
    #if the current node is a leaf return pathSum
    if currentNode.left is None and currentNode.right is None:
        return pathSum
    #traverse the left and right sub-tree
    return find_root_to_leaf_pathNumbers(currentNode.left, pathSum) + find_root_to_leaf_pathNumbers(currentNode.right, pathSum)

    #     12
    #    /  \
    #   7    1
    #  /    / \
    # 4   10   5
             
root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
sum = 23
print(find_sum_of_path_number(root))


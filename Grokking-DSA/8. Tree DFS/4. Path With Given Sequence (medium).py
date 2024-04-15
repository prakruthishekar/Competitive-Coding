# Given a binary tree and a number sequence, find if the sequence is present 
# as a root-to-leaf path in the given tree.


# Sequence: [1, 9, 9]
# Output: true
# Explaination: The tree has a path 1 -> 9 -> 9.



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None


def find_path(root, sequence):
    if not root:
        return len(sequence) == 0
    return find_all_paths_recursive(root,sequence, 0)


def find_all_paths_recursive(currentNode, sequence, sequenceIndex):
    if currentNode is None:
        return False

    seqLen = len(sequence)
    if sequenceIndex >= seqLen or currentNode.val != sequence[sequenceIndex]:
        return False

    #if the current node is a leaf and it's value is equal to the sum, we'hv found the path
    if currentNode.left is None and currentNode.right is None and sequenceIndex == seqLen - 1:
        return True
        # print(currentPath)

    return find_all_paths_recursive(currentNode.left, sequence,sequenceIndex + 1) \
        or find_all_paths_recursive(currentNode.right, sequence,sequenceIndex + 1)

#     1
#    / \
#   0   1
#  /   / \
# 1   6   5
      
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)
sum = 23
print(find_path(root,[1,0,7]))
print(find_path(root,[1,1,6]))



# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None

def isSymmetric(root):
        stack = []
        if root: stack.append([root.left, root.right])

        while(len(stack) > 0):
            left, right = stack.pop()
            
            if left and right:
                if left.val != right.val: return False
                stack.append([left.left, right.right])
                stack.append([right.left, left.right])
        
            elif left or right: return False
        
        return True


    
def isSymmetric(root) -> bool:
    if root==None:
        return True
    
    def getResult(left,right):

        if left==None and right==None:
            return True
        if left==None or right==None or left.val != right.val:
            return False

        return getResult(left.left,right.right) and getResult(left.right,right.left)
    
    return getResult(root.left,root.right)



#       1
#      / \
#     2   2
#    / \ / \
#   3  4 4  3

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(isSymmetric(root=root))
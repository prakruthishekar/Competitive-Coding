class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if root.value == value:
            return root
        elif root.value < value:
            root.right = insert(root.right, value)
        else:
            root.left = insert(root.left, value)
    return root

def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return max(left_height, right_height) + 1

# Example usage:
root = Node(5)
insert(root, 3)
insert(root, 8)
insert(root, 1)
insert(root, 4)
insert(root, 7)
insert(root, 10)

print(height(root))  # Output: 3

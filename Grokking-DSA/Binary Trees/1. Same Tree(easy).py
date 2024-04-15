
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false



from collections import deque


def isSameTree(p, q) -> bool:
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """    
    # p and q are both None
    if not p and not q:
        return True
    # one of p and q is None
    if (not q or not p) or (p.val != q.val):
        return False
    return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
    


    # iterative DFS
def isSameTree(p,q):
    stack =[(p,q)]
    while stack:
        p,q = stack.pop()
        if not p and not q:
            continue
        elif (not p or not q) or (p.val !=q.val):
            return False
        stack.extend([(q.right,p.right),(q.left,p.left)])
    return True


# iterative BFS
def isSameTreeBFS(p,q):
    queue = deque([(p, q)])  # Enqueue both nodes as tuples
    while queue:
        p, q = queue.popleft()  # Dequeue a tuple
        if not p and not q:
            continue
        elif (not p or not q) or (p.val != q.val):
            return False
        queue.append((p.left if p else None, q.left if q else None))  # Enqueue left child nodes
        queue.append((p.right if p else None, q.right if q else None))  # Enqueue right child nodes
    return True



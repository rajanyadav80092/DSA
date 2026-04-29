class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
    
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
        
from collections import deque

def level_order(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right) 
        
    
def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def tree_sum(root):
    if not root:
        return 0
    return root.data  + tree_sum(root.right)

#advance problem 
def diameter(root):
    def helper(node):
        if not node:
            return 0, 0

        lh, ld = helper(node.left)
        rh, rd = helper(node.right)

        height = 1 + max(lh, rh)
        dia = max(lh + rh + 1, ld, rd)

        return height, dia

    return helper(root)[1]

#lowest common ancestor
def lca(root, p, q):
    if not root:
        return None

    if root.data == p or root.data == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root

    return left if left else right

def max_value(root):
    if not root:
        return float("-inf")
    left=max_value(root.left)
    right=max_value(root.right)
    return max(root.data,left,right)

def height(root):
    if not root:
        return 0
    
    return 1+max(height(root.left),height(root.right))
def counat_nodes(root):
    if not root:
        return 0
    return 1+count_nodes(root.left)+count_nodes(root.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
# inorder(root)
# print("postorder")
# postorder(root)
# print("preorder")
# preorder(root)
# print("level order")
# level_order(root)
# print("count")
# print(count_nodes(root))
# print("height")
# print(height(root))
# print("tree_sum")
# print(tree_sum(root))
# print("diameter")
# print(diameter(root))
# print("lca")
# print(lca(root,2,4))
# print("max_value")
# print(max_value(root))
print("count")
print(counat_nodes(root))
# Tree example

#      1
#   2     3
# 4  5  10  

# Binary tree with time and space :O(n)

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)  # optional part to print the node if no display function is written

# Initialize a tree 
   
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

# Rucurssive Approach
# Preorder traversal DFS O(n)

def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)

pre_order(A)

###################################################
print()

# Inorder Traversal DFS O(n)

def in_order(node):
    if not node:
        return
    
    in_order(node.left)
    print(node)
    in_order(node.right)

in_order(A)

########################################
print()

# Post order traversal O(n)

def post_order(node):
    if not node:
        return
    
    post_order(node.left)
    post_order(node.right)
    print(node)

post_order(A)


print()
#####################################################################################################################  
print()

# Iterative approach using stack or call stack for preorder  O(n)

def iterative_pre_order(node):
    stk = [node]
    while stk:
        node = stk.pop()
        print(node)
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)
iterative_pre_order(A)

print()


##############################################################

# Level order traversal BFS O(N)
from collections import deque
q = deque()
def level_order(node):
    q.append(node)
    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

level_order(A)

###########################################################
print()
# Search Using DFS IN O(n)

def search(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    return search(node.left, target) or search(node.right, target)

print(search(A, 5))

    





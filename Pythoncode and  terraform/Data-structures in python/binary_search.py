# Normal way of searching as O(N)
A = [1,2,3,4,5,-3,-2]

if 2 in A:
    print(True)
else:
    print(False)

######################################

# Binary search in Time:O(logN) SPACE:O(1)

def binary_search(arr, target):
    N = len(arr)
    L = 0
    R = N-1
    while L <= R:
        M = L + ((R-L)//2)   # WE CAN USE (R+L)//2 INSTEAD BUT IN LARGE NUMBERS IT CREATES A PROBLEM
        if arr[M] == target:
            return True
        elif target < arr[M]:
            R = M-1
        else:
            L = M+1
    return False

print(binary_search(A, 3))

####################### Binary search trees###########################

#          5
#      1       8
#   -1   3   7    9

class binaryTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    
A2 = binaryTree(5)
B2 = binaryTree(1)
C2 = binaryTree(8)
D2 = binaryTree(-1)
E2 = binaryTree(3)
F2 = binaryTree(7)
G2 = binaryTree(9)    

A2.left = B2
A2.right = C2
B2.left = D2
B2.right = E2
C2.left = F2
C2.right = G2

###############################
# Search in a BST O(log(n)) in average case butworst case is O(n) when tree is skeewed

def search_bst(node , target):
    if not node:
        return False
    if node.val == target:
        return True
    if target < node.val: return search_bst(node.left, target)
    else: return search_bst(node.right, target)

search_bst(A2, 5)
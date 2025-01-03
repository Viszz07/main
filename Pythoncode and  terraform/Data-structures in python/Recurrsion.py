# Fibbonachi sequence using recurrsion  Time O(2^n)   Space: O(n)

def F(n):
    if n==0: return 0
    if n==1: return 1
    return F(n-1) + F(n-2)

print(F(12))

# Linked list using recurrsion to print the elements in reverse

class SingleLL:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):         # Optional part if you just want to check the print function of the class
        return str(self.val)
    
# OR You can import the linkelist class from linkedlist file 
# from LinkedList import SingleLL

Head = SingleLL(1)
A = SingleLL(5)
B = SingleLL(10)
C = SingleLL(15)

Head.next = A
A.next = B
B.next = C

def reverse(node):
    if not node:
        return
    
    reverse(node.next)
    print(node)

reverse(Head)


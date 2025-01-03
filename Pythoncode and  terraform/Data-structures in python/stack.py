# Stack is just a list while appending

stack = []

# Adding an element to a stack O(1)
stack.append(1)                 
stack.append(2)                 
stack.append(3)                 
stack.append(4)                 

# Removing or popping an element from the stack or stack.pop(-1)  O(1)

print(stack.pop())

# Printing the stack from top to bottom

while stack:
    print(stack.pop())


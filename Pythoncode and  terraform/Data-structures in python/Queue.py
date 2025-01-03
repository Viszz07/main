from collections import deque

q = deque()

# Adding elements in an queue O(1)
q.append(1)                 
q.append(2)                 
q.append(3)                 
q.append(4) 

# other option to add eleements for testing
for n in range(5,10):
    q.append(n)
print(q)

# Removing element from queue FIFO O(1)

print(q.popleft())

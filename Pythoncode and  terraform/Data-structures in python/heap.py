# Heapify usues Time O(N) SPACE O(1)
import heapq
A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
heapq.heapify(A)             # Min Heap 
print(A)


print()
# Heap Sort
# Time: O(n log n), Space: O(n)
# NOTE: O(1) Space is possible via swapping, but this is complex

def heapsort(arr):
  heapq.heapify(arr)
  n = len(arr)
  new_list = []

  for i in range(n):
    minn = heapq.heappop(arr)
    new_list.append(minn)

  return new_list

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))



print()
# Putting tuples of items on the heap

D = [5, 4, 3, 5, 4, 3, 5, 5, 4]

from collections import Counter

counter = Counter(D)
print(counter)
heap = []

for k, v in counter.items():
  heapq.heappush(heap, (v, k))

print(heap)
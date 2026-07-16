from collections import deque

dq=deque([1, 2, 3, 4, 5])
dq.append(6)  # Add to the right
dq.appendleft(0)  # Add to the left
print(dq)  # Output: deque([0, 1, 2, 3, 4, 5, 6])

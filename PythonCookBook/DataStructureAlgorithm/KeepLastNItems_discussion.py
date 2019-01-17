from collections import deque

# Using deque(maxlen=N) creates a fixed sized queue. When a new items are added and the queue is full, 
# the oldest item is automatically removed.
# e.g.
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q);
q.append(4)
print(q);
q.append(5)
print(q);

# More generally, a deque can be used whenever we need a simple queue structure.
# If we don't give it a maximum size, we get an unbounded queue that lets us append
# and pop items on either end. E.g.

q1 = deque()
q1.append(1)
q1.append(2)
q1.append(3)
print(q1)
q1.appendleft(4)
print(q1)
q1.pop()
print(q1)
q1.popleft()
print(q1)



from collections import deque
n = int(input())
queue = deque(range(1,1+n))
a = []
while len(queue) > 1:
    a.append(queue.popleft())
    queue.append(queue.popleft())
a.append(queue.popleft())
print(*a)
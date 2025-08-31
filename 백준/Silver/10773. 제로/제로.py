from collections import deque

n = int(input())
queue = deque()
result = 0

for i in range(n):
    a = int(input())
    if a != 0:
        queue.append(a)
    else:
        queue.pop()

for i in range(len(queue)):
    result += queue.popleft()

print(result)
import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
queue = deque()
result = []

for i in range(1, N + 1):
    command = data[i].split()
    a = command[0]
    b = command[1] if len(command) > 1 else None

    if a == "push":
        queue.append(b)
    elif a == "pop":
        if not queue:
            result.append(-1)
        else:
            result.append(queue.popleft())
    elif a == "size":
        result.append(len(queue))
    elif a == "empty":
        result.append(1 if not queue else 0)
    elif a == "front":
        if not queue:
            result.append(-1)
        else:
            result.append(queue[0])
    elif a == "back":
        if not queue:
            result.append(-1)
        else:
            result.append(queue[-1])

sys.stdout.write("\n".join(map(str, result)) + "\n")
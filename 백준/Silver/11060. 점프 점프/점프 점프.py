from collections import deque

n = int(input())
maze = list(map(int, input().split()))
visited = [False] * n

queue = deque()
queue.append((0,maze[0],0))
visited[0] = True
# 위치, 값, 카운트

while queue:
    position, value, count = queue.popleft()

    if position == n - 1:
        print(count)
        exit()

    for i in range(1, value+1):
        next_position = position + i
        if next_position < n and visited[next_position] == False:
            visited[next_position] = True
            queue.append((next_position, maze[next_position], count + 1))
print(-1)


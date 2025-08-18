from collections import deque

n, m  = map(int,input().split())
maze = [list(input()) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0,0,1))
visit[0][0] = True

while queue:
    x, y, dist = queue.popleft()
    
    if x == n-1 and y == m-1:
        print(dist)
        break
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0<= ny < m:
            if not visit[nx][ny] and maze[nx][ny] == '1':
                visit[nx][ny] = True
                queue.append((nx, ny, dist+1))



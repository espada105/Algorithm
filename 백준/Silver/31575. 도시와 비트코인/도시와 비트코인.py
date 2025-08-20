from collections import deque

n,m = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]

queue = deque([(0, 0)])
visited[0][0] = 1

if maze[0][0] == 0:
    print("No")
    exit()

dx = [1, 0]
dy = [0, 1]

while queue:
    x, y = queue.popleft()

    if x == n-1 and y == m-1:
        print('Yes')
        exit()
    
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0<= ny < m and visited[ny][nx] == 0 and maze[ny][nx] == 1:

            visited[ny][nx] = 1
            queue.append((nx,ny))
        

print('No')


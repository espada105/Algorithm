from collections import deque

start_x, start_y = map(int, input().split())
end_x, end_y = map(int, input().split())

start_x -= 1
start_y -= 1
end_x -= 1
end_y -= 1

graph = [[0 for _ in range(8)] for _ in range(8)]

queue = deque()
queue.append((start_x,start_y,0))

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]

while queue:
    x, y, count = queue.popleft()

    if x == end_x and y == end_y:
        print(count)
        exit()

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= 7 and 0 <= ny <= 7 and graph[ny][nx] == 0:
            graph[ny][nx] = 1
            queue.append((nx, ny, count + 1))
            

from collections import deque

w, h = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(h)]

cnt = 0

queue = deque()

for y in range(h):
    for x in range(w):
        if grid[y][x] == 1:
            queue.append((y,x))


while queue:
    size = len(queue)
    has_spread = False

    for _ in range(size):
        y,x = queue.popleft()

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ry, rx = dy + y, dx + x
            if 0 <= rx < w and 0 <= ry < h:
                if grid[ry][rx] == 0:
                    grid[ry][rx] = 1
                    queue.append((ry,rx))
                    has_spread = True
    if has_spread:
        cnt +=1
            
for row in grid:
    if 0 in row:
        print(-1)
        exit()

print(cnt)
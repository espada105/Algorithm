from collections import deque

N = int(input())

for i in range(N):
    h,w = map(int,input().split())
    grid = [list(input().strip()) for _ in range(h)]
    cnt = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] == "#":
                cnt += 1
                queue = deque([(r,c)])
                grid[r][c] = "."

                while queue:
                    x, y = queue.popleft()
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = x + dr, y + dc

                        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == "#":
                            grid[nr][nc] = "."
                            queue.append((nr,nc))
    print(cnt)
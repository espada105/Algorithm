from collections import deque
import sys

h, w = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(h)] 

queue = deque()

for x in range(w):
    if grid[0][x] == '0':
        queue.append((0, x))
        grid[0][x] = '1'

        while queue:
            ry, rx = queue.popleft()
            
            if ry == h - 1:
                print("YES")
                exit()
            
            for ty, tx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ny, nx = ry + ty, rx + tx 
                
                if 0 <= nx < w and 0 <= ny < h:
                    if grid[ny][nx] == '0':
                        grid[ny][nx] = '1'
                        queue.append((ny, nx))

print("NO")
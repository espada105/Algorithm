import sys
from collections import deque

input = sys.stdin.readline

def bfs(y, x, h, w, grid):
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    
    queue = deque([(y, x)])
    grid[y][x] = 0  
    
    while queue:
        cy, cx = queue.popleft()
        for i in range(8):
            ny, nx = cy + dy[i], cx + dx[i]
            
            if 0 <= ny < h and 0 <= nx < w:
                if grid[ny][nx] == 1:
                    grid[ny][nx] = 0 
                    queue.append((ny, nx))


while True:
    line = input().split()
    if not line: break
    
    w, h = map(int, line)
    
    if w == 0 and h == 0:
        break
        
    grid = [list(map(int, input().split())) for _ in range(h)]
        
    island_count = 0
    
    for i in range(h):
        for j in range(w):
            
            if grid[i][j] == 1:
                island_count += 1
                
                bfs(i, j, h, w, grid)
    
    print(island_count)
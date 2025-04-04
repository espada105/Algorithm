import sys
sys.setrecursionlimit(10000)

def dfs(y, x, field, N, M):
    if not (0 <= y < N and 0 <= x < M) or field[y][x] == 0:
        return
    
    field[y][x] = 0
    
    dfs(y-1, x, field, N, M)  
    dfs(y+1, x, field, N, M)  
    dfs(y, x-1, field, N, M)  
    dfs(y, x+1, field, N, M)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    
    field = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1
    
    worm_count = 0
    
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1:
                dfs(y, x, field, N, M)
                worm_count += 1
    
    print(worm_count)
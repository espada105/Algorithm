N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]

for ii in range(N):
    for i in range(N):
        for iii in range(N):
            if graph[i][ii] == 1 and graph[ii][iii] == 1:
                graph[i][iii] = 1

for i in graph:
    print(' '.join(map(str, i)))
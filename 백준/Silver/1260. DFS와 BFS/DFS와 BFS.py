from collections import deque 

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N+1):
    graph[i].sort()


def dfs(graph, v, visited, result):
    visited[v] = True
    result.append(v)

    for nextnode in graph[v]:
        if not visited[nextnode]:
            dfs(graph, nextnode, visited, result)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    result = []
    
    while queue:
        v = queue.popleft()
        result.append(v)

        for nextnode in graph[v]:
            if not visited[nextnode]:
                queue.append(nextnode)
                visited[nextnode] = True
    
    return result


visited_dfs = [False] * (N + 1)
dfs_result = []
dfs(graph, V, visited_dfs, dfs_result)
print(' '.join(map(str, dfs_result)))

visited_bfs = [False] * (N + 1)
bfs_result = bfs(graph, V, visited_bfs)
print(' '.join(map(str, bfs_result)))
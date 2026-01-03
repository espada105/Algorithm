import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (N + 1)
count = 0

for i in range(1, N + 1):
    if not visited[i]:
        count += 1
        queue = deque([i])
        visited[i] = True
        
        while queue:
            curr = queue.popleft()
            
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

print(count)
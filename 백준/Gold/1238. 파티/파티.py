import sys
from heapq import heappop, heappush

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, node = heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heappush(pq, (new_dist, neighbor))
    
    return dist

def solution(N, M, X, edges):
    graph = [[] for _ in range(N+1)]
    for u, v, w in edges:
        graph[u].append((v, w))
    
    max_time = 0
    for i in range(1, N+1):
        if i == X:
            continue
        dist_from_i_to_X = dijkstra(graph, i)[X]
        dist_from_X_to_i = dijkstra(graph, X)[i]
        total_time = dist_from_i_to_X + dist_from_X_to_i
        max_time = max(max_time, total_time)
    
    return max_time

N, M, X = map(int, sys.stdin.readline().split())
edges = []
for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((u, v, w))

print(solution(N, M, X, edges))

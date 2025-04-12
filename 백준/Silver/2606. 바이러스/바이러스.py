from collections import deque

computer = int(input())
edge = int(input())
check = deque([1])

graph = [[] for _ in range(computer + 1)]

for _ in range(edge):
    n,m = map(int,input().split())
    graph[n].append(m)
    graph[m].append(n)

def search(n):
    for i in graph[n]:
        if i not in check:
            check.append(i)
            search(i)

search(1)
print(len(check)-1)
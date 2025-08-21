from collections import deque

n = int(input())
a, b = map(int,input().split())

m = int(input())
relation = [list(map(int,input().split())) for _ in range(m)]

people = [[] for _ in range(n + 1)] # 전체 사람
visited = [0] * (n + 1)

for x, y in relation: #x : 부모 y: 자식
    people[x].append(y)
    people[y].append(x)

queue =deque([(a, 0)])
visited[a] = 1

while queue:
    pos, count = queue.popleft()
    
    if pos == b:
        print(count)
        exit()

    for i in people[pos]:
        if visited[i] == 0:
            queue.append((i, count + 1))
            visited[i] = 1
            

print(-1)
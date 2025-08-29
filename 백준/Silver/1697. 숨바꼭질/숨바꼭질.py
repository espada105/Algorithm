from collections import deque

m, n = map(int,input().split())
queue = deque([(m,0)])
visited = [False] * 100001

while queue:
    m,count = queue.popleft()
    
    if m == n:
        print(count)
        break
    
    if m >= 0 and m <= 100000:
        if m * 2 <= 100000 and not visited[m * 2]:
            visited[m * 2] = True
            queue.append((m * 2, count+1))
        if m + 1 <= 100000 and not visited[m + 1]:
            visited[m + 1] = True
            queue.append((m + 1, count+1))
        if m - 1 >= 0 and not visited[m - 1]:
            visited[m - 1] = True
            queue.append((m - 1, count+1))
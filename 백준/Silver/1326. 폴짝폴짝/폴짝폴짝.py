from collections import deque

n = int(input())
bridge = list(map(int, input().split()))
start, end = map(int, input().split())

if start == end:
    print(0)
    exit()

visited = [False] * n
queue = deque([start-1])
visited[start-1] = True
count = 0

while queue:
    count += 1
    size = len(queue)
    
    for _ in range(size):
        position = queue.popleft()
        num = bridge[position]
        
        next_pos = position + num
        while next_pos < n:
            if next_pos == end - 1:
                print(count)
                exit()
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append(next_pos)
            next_pos += num
        
        next_pos = position - num
        while next_pos >= 0:
            if next_pos == end - 1:
                print(count)
                exit()
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append(next_pos)
            next_pos -= num

print(-1)
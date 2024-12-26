from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    priorities = list(map(int, input().split()))
    
    dequelist = deque((i, priorities[i]) for i in range(n))
    count = 0
    
    while dequelist:
        current = dequelist.popleft()
        
        if any(current[1] < doc[1] for doc in dequelist):
            dequelist.append(current)
        else:
            count += 1
            if current[0] == m:
                print(count)
                break

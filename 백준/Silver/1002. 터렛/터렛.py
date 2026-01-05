import math

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())

    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    if distance == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    
    elif distance == r1 + r2 or distance == abs(r1 - r2):
        print(1)
    
    elif distance > r1 + r2 or distance < abs(r1 - r2):
        print(0)
    
    else:
        print(2)
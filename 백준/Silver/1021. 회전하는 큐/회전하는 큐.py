from collections import deque

n, m = map(int, input().split())
target_order = list(map(int, input().split()))

queue = deque(range(1, n+1))
count = 0

for target in target_order:
    left_distance = queue.index(target)
    right_distance = len(queue) - left_distance
    
    if left_distance <= right_distance:
        queue.rotate(-left_distance)
        count += left_distance
    else:
        queue.rotate(right_distance)
        count += right_distance
    
    queue.popleft()

print(count)
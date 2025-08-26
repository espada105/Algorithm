from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
queue = deque()
max_count = 0
student_num = 0

for _ in range(n):
    line = input().strip()
    
    if line.startswith('1'):
        student_id = int(line.split()[1])
        queue.append(student_id)
        
        if len(queue) > max_count:
            max_count = len(queue)
            student_num = student_id
        elif len(queue) == max_count:
            if student_id < student_num:
                student_num = student_id
    else:
        queue.popleft()

print(f"{max_count} {student_num}")
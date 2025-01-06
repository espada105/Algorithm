import sys
import heapq

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
if n == 1:
    print(0)
    exit()

dasom = int(data[1])
others = [-int(data[i]) for i in range(2, n+1)]
heapq.heapify(others)

count = 0
while -others[0] >= dasom:
    max_votes = -heapq.heappop(others)
    max_votes -= 1
    dasom += 1
    count += 1
    heapq.heappush(others, -max_votes)

print(count)
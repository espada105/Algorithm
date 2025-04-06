import sys

n, m = map(int,sys.stdin.readline().split())

pocketmon = [sys.stdin.readline().strip() for _ in range(n)]
problem = {name: i + 1 for i, name in enumerate(pocketmon)}

for _ in range(m):
    query = sys.stdin.readline().strip()
    if query.isdigit():
        idx = int(query) - 1
        print(pocketmon[idx])
    else:
        print(problem[query])
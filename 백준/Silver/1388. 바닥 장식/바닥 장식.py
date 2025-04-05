N, M = map(int, input().split())
floor = []
for i in range(N):
    floor.append(input())

count = 0

for i in range(N):
    j = 0
    while j < M:
        if floor[i][j] == '-':
            count += 1
            while j < M and floor[i][j] == '-':
                j += 1
        else:
            j += 1

for j in range(M):
    i = 0
    while i < N:
        if floor[i][j] == '|':
            count += 1
            while i < N and floor[i][j] == '|':
                i += 1
        else:
            i += 1

print(count)
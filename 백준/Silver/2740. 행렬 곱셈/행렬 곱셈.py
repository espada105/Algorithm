n, m = map(int, input().split())
matrix_a = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
matrix_b = [list(map(int, input().split())) for _ in range(m)]

result = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            result[i][j] += matrix_a[i][l] * matrix_b[l][j]

for ii in result:
    print(' '.join(map(str, ii)))
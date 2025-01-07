import sys

input = sys.stdin.read().splitlines()

T = int(input[0])

apt = [[0]*15 for _ in range(15)]

for i in range(1, 15):
    apt[0][i] = i

for i in range(1, 15):
    for j in range(1,15):
        apt[i][j] = apt[i-1][j] + apt[i][j-1]

for i in range(T):
    k = int(input[2 * i + 1])
    n = int(input[2 * i + 2])
    print(apt[k][n])
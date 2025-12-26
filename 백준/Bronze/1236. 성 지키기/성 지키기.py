import sys
input = sys.stdin.read().split()

N, M = int(input[0]), int(input[1])
castle = input[2:]

row_needed = sum(1 for i in range(N) if 'X' not in castle[i])


col_needed = sum(1 for j in range(M) if 'X' not in [castle[i][j] for i in range(N)])

print(max(row_needed, col_needed))
n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
cycles = {
    0: [10],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1],
}
result = []
for a, b in num:
    d = a % 10
    cycle = cycles[d]
    idx = (b - 1) % len(cycle)
    result.append(str(cycle[idx]))

print('\n'.join(result))
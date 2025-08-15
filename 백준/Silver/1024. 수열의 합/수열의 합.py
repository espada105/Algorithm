n, l = map(int, input().split())

for length in range(l, 101):
    if 2 * n % length != 0:
        continue

    start = (2 * n // length - length + 1) // 2

    if start < 0:
        continue

    result = list(range(start, start + length))
    if sum(result) == n:
        print(' '.join(map(str, result)))
        exit()
    
print(-1)
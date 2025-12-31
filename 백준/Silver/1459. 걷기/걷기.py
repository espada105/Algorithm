import sys

x, y, w, s = map(int, sys.stdin.readline().split())

case1 = (x + y) * w

case2 = min(x, y) * s + abs(x - y) * w

if (x + y) % 2 == 0:
    case3 = max(x, y) * s
else:
    case3 = (max(x, y) - 1) * s + w

print(min(case1, case2, case3))
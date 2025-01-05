from collections import Counter
import sys
input = sys.stdin.read

data = input().split()
M = int(data[0])
Mlist = Counter(map(int, data[1:M+1]))
N = int(data[M+1])
Nlist = map(int, data[M+2:])

result = [Mlist[i] if i in Mlist else 0 for i in Nlist]

print(*result)

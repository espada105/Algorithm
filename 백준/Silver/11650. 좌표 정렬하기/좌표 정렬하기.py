import sys
n=int(sys.stdin.readline())
listn=[]
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    listn.append([a, b])
listn.sort()
for i in listn:
    print(i[0], i[1])
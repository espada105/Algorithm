M = int(input())
Mlist = list(map(int, input().split()))
N = int(input())
Nlist = list(map(int, input().split()))

Mdict = {x: True for x in Mlist}

for i in Nlist:
    if i in Mdict:
        print(1)
    else:
        print(0)
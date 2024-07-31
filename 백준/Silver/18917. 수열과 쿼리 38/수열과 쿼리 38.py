import sys
n=int(sys.stdin.readline())
sum=0
q=0
for i in range(n):
    w=list(map(int,sys.stdin.readline().split()))
    if w[0]== 1:
        sum+=w[1]
        q = q^w[1]
    elif w[0]== 2 :
        sum-=w[1]
        q=q^w[1]
    elif w[0] == 3: print((sum))
    elif w[0] == 4: print(q)
n = int(input())
s,m,l,xl,xxl,xxxl = map(int,input().split())
t,p = map(int,input().split())
count = 0
for i in [s,m,l,xl,xxl,xxxl]:
    count += (i + t -1) // t
print(count)
print(n//p,n%p)


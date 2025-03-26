N, M = map(int, input().split())
group = []
invid = []
for i in range(M):
    a, b = map(int,input().split())
    group.append(a)
    invid.append(b)

quotient = N // 6
remainder = N % 6 
#M 1개당 00원

result = []
#group
result.append(min(group) * (quotient+1))
#group  invid
result.append(min(group) * (quotient) + min(invid) * remainder)
#invid
result.append(min(invid) * N)

print(min(result))
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
result = 0
a.sort()
index_b = sorted(b,reverse=True)

for i in b:
    index = index_b.index(i)
    result += i * a[index]
    index_b[index] = None

print(result)
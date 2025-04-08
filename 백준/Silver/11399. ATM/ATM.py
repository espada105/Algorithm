n = int(input())
m = sorted(list(map(int,input().split())))
result = [0] * (n + 1)
result[0] = m[0]
for i in range(1,n):
    result[i] = result[i-1] + m[i]

print(sum(result))
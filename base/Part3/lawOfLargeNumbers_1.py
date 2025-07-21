n,m,k = map(int,input().split())

data = sorted(list(map(int,input().split())))

# m은 전체, k는 최대연속가능
result = 0

while m != 0:
    if m >= k:
        m -= k
        result += data[-1] * k
        data.pop()
    else:
        result += data[-1] *m
        m = 0
        



print(result)
n,m,k = map(int,input().split())

data = sorted(list(map(int,input().split())))

# m은 전체, k는 최대연속가능
result = 0

first = data[-1]
second = data[-2]

# 가장 큰 수가 반복되는 횟수 int(M/(K+1)) * K + M % (K+1)
count = int(m / (k + 1)) * k 
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second
print(result)
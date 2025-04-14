N, M = map(int, input().split())
num = list(map(int, input().split()))

prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + num[i]

result = []
for _ in range(M):
    a, b = map(int, input().split())
    result.append(prefix_sum[b] - prefix_sum[a-1])

for i in result:
    print(i)
K, N = map(int, input().split())

lines = list()
for i in range(K):
    lines.append(int(input()))

lines.sort()
minLength = 1
maxLength = lines[len(lines) - 1]

cnt = 0

while minLength <= maxLength:
    cnt = 0
    midLength = (minLength + maxLength) // 2
    for line in lines:
        cnt += line // midLength

    if cnt >= N:
        minLength = midLength + 1
    else:
        maxLength = midLength - 1

print(minLength - 1)
n = int(input())
friend = [list(input()) for _ in range(n)]
result = []

for i in range(n):
    count = 0
    for j in range(n):
        if i == j:
            continue
            
        if friend[i][j] == 'Y':
            count += 1
        else:
            for k in range(n):
                if friend[i][k] == 'Y' and friend[k][j] == 'Y':
                    count += 1
                    break
                    
    result.append(count)

print(max(result))
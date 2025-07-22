n = int(input())
count = 0

for i in range(n+1):
    for ii in range(60):
        for iii in range(60):
            if '3' in str(i) + str(ii) + str(iii):
                count += 1

print(count)
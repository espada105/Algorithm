x = int(input())
stick = [64, 32, 16, 8, 4, 2, 1]
n = 0

for i in range(len(stick)):
    if x >= stick[i]:
        n += 1
        x -= stick[i]
    if x == 0:
        break
print(n)
string = input()
n = int(input())
count = 0
for i in range(n):
    ring = input()
    if string in ring * 2:
        count += 1

print(count)
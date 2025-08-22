n = list(map(int, input().strip()))

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in n:
    count[i] += 1

sum69 = count[6] + count[9]
combined = (sum69 + 1) // 2

count[6] = count[9] = 0
max_others = 0
for i in range(10):
    if max_others < count[i]:
        max_others = count[i]

print(max(combined, max_others))
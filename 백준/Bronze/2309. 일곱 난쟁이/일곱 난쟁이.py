import sys

nanjang = [int(sys.stdin.readline()) for _ in range(9)]
nanjang.sort()

total_sum = sum(nanjang)
target = total_sum - 100

fake_a, fake_b = -1, -1

for i in range(9):
    for j in range(i + 1, 9):
        if nanjang[i] + nanjang[j] == target:
            fake_a, fake_b = i, j
            break
    if fake_a != -1:
        break

for k in range(9):
    if k == fake_a or k == fake_b:
        continue
    print(nanjang[k])
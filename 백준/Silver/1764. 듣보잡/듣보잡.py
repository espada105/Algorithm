n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    a.append(input())

for i in range(m):
    b.append(input())

answer = sorted((set(a) & set(b)))

print(len(answer))

for i in answer:
    print(i)

day = int(input())
tree = sorted(list(map(int,input().split())))
tree.reverse()


result = []
for i in range(day):
    result.append(tree[i] + i + 2)

print(max(result))


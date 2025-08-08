n = list(input())
m = [int(i) for i in n]
m.sort(reverse=True)
print(''.join(map(str,(m))))
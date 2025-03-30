a, b = map(int,input().split())

lista = set(map(int,input().split()))
listb = set(map(int,input().split()))

unionAB = len(lista | listb) - len(lista & listb)

print(unionAB)
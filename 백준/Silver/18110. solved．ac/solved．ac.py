import sys

n = int(sys.stdin.readline().strip())

def newRound(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

lista = []
for i in range(n):
    lista.append(int(sys.stdin.readline().strip()))

lista.sort()

minus = newRound(n * 0.15)

resultList = lista[minus:n-minus]

if resultList:
    resultList = newRound(sum(resultList)/len(resultList))
    print(resultList)
else:
    print(0)
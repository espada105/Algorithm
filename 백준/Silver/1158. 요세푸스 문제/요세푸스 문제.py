n, k = map(int, input().split())

listk = [i + 1 for i in range(n)]
resultList = []
index = 0

for i in range(n):
    index = (index + k - 1) % len(listk)
    resultList.append(listk.pop(index)) 


print("<" + ", ".join(map(str, resultList)) + ">")

coin = [25,10,5,1]
testcase = int(input())
result = []
for i in range(testcase):
    n = int(input())
    coins = []
    for ii in range(4):
        a = n // coin[ii]
        n = n - a * coin[ii]
        coins.append(a)
    result.append(coins)

for k in result:
    print(" ".join(map(str,k)))
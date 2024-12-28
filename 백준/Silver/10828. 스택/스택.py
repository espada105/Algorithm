import sys

input = sys.stdin.read
inputs = input().splitlines()

n = int(inputs[0])
resultList = []
results = []

for i in range(1, n + 1):
    command = inputs[i].split()

    if command[0] == "push":
        num = int(command[1])
        resultList.append(num)
    elif command[0] == "pop":
        if not resultList:
            results.append(-1)
        else:
            results.append(resultList.pop())
    elif command[0] == "size":
        results.append(len(resultList))
    elif command[0] == "empty":
        results.append(1 if not resultList else 0)
    elif command[0] == "top":
        if not resultList:
            results.append(-1)
        else:
            results.append(resultList[-1])

sys.stdout.write("\n".join(map(str, results)) + "\n")

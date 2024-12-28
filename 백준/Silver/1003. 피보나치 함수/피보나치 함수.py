import sys

input = sys.stdin.read
inputs = input().splitlines()

n = int(inputs[0])
cases = list(map(int, inputs[1:]))

fibo = [[0, 0] for _ in range(41)]
fibo[0] = [1, 0] 
fibo[1] = [0, 1]

for i in range(2, 41):
    fibo[i][0] = fibo[i - 1][0] + fibo[i - 2][0]
    fibo[i][1] = fibo[i - 1][1] + fibo[i - 2][1]

results = []

for n in cases:
    results.append(f"{fibo[n][0]} {fibo[n][1]}")

sys.stdout.write("\n".join(results) + "\n")

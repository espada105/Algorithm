import sys

N = int(sys.stdin.readline())

first = []
for _ in range(N):
    first.append(sys.stdin.readline().strip())

if N == 1:
    print(first[0])
else:
    pattern = list(first[0])

    for i in range(1, N):
        current_file = first[i]
        for j in range(len(pattern)):
            if pattern[j] != '?' and pattern[j] != current_file[j]:
                pattern[j] = '?'

    print("".join(pattern))
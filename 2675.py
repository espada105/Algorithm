T = int(input())

for i in range(T):
    R, S = input().split()
    P = []
    for i in range(0, len(S)):
        P.append(S[i] * int(R))
    print(''.join(P))

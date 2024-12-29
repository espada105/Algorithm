def solution():
    res = []
    N, X = list(map(int, input().split()))
    A = list(map(int, input().split()))

    Aj = [[i+1, (A[i]-1)//X] for i in range(len(A))]

    Aj.sort(key=lambda x : x[1])

    answer = " ".join([str(a[0]) for a in Aj])
    return answer

N = int(input())
for i in range(N):
    result = solution()
    print("Case #{}: {}".format(i+1, result))
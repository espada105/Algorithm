def backtrack(arr, start, n, m):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(start, n + 1):
        arr.append(i)
        backtrack(arr, i, n, m)
        arr.pop()

n, m = map(int, input().split())
backtrack([], 1, n, m)
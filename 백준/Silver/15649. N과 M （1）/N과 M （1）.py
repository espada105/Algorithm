n, m = map(int,input().split())

def backtrack(arr,start,n,m):
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(1,n+1):
        if i not in arr:
            arr.append(i)
            backtrack(arr,start + 1,n,m)
            arr.pop()

backtrack([],1,n,m)


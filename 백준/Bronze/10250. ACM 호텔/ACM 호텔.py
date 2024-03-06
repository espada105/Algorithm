T = int(input())
for i in range(T):
    H,W,N = map(int,input().split())

    roomnumber = N // H + 1
    stair = N % H

    if stair == 0:
        roomnumber -= 1
        stair = H
    print(stair * 100 + roomnumber)
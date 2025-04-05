import sys

# 입출력 속도 향상을 위한 설정
input = sys.stdin.readline
print = sys.stdout.write

S = set()
M = int(input())

for _ in range(M):
    command = input().strip().split()
    
    if command[0] == "add":
        S.add(int(command[1]))
    
    elif command[0] == "remove":
        if int(command[1]) in S:
            S.remove(int(command[1]))
    
    elif command[0] == "check":
        if int(command[1]) in S:
            print("1\n")
        else:
            print("0\n")
    
    elif command[0] == "toggle":
        num = int(command[1])
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    
    elif command[0] == "all":
        S = set(range(1, 21))
    
    elif command[0] == "empty":
        S = set()
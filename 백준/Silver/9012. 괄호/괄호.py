n = int(input())

for _ in range(n):
    list_n = list(input()) 
    sum = 0

    for i in range(len(list_n)):
        if list_n[i] == "(":
            sum += 1
        else:
            sum -= 1
        
        if sum < 0:
            print("NO")
            break
    else:
        if sum == 0:
            print("YES")
        else:
            print("NO")

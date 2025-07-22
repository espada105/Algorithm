n = int(input())
plan = list(map(str, input().split()))
L = 1
R = 1

for i in plan:
    if i == "L" :
        L -= 1
    elif i == "R":
        L += 1
    elif i == "U":
        R += 1
    else:
        R -= 1

    if L <= 1:
        L = 1
    if R <= 1:
        R = 1


print(L,R)
a,b=map(int,input().split())
c = 60

if(b<45):
    if(a==0):
        a = 23
        b -= 45
        b = c + b
        print(a, b)
    else:
        a -= 1
        b -= 45
        b = c + b
        print(a, b)
else:
    if(a==0):
        a = 23
        b -= 45
        print(a, b)
    else:
        a -= 1
        b -= 45
        print(a, b)
 


n = int(input())

rectangle = [0] * (n+1)

if n == 1:
    result = 1
    print(1)
else:
    rectangle[1] = 1
    rectangle[2] = 2

    for i in range(3,n+1):
        rectangle[i] = ((rectangle[i-1] % 10007)+ (rectangle[i-2] % 10007))  % 10007
    print(rectangle[n])

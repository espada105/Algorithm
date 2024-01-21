def f(n):
    a = 1
    for i in range(1,n):
        a *= i
    return a
test = int(input())

for i in range(test):
    n,m = map(int,input().split())
    print(f(m)//(f(n)*f(m-n)))


num = int(input())
lista =[]
for i in range(num):
    x = input()
    if x not in lista:
        lista.append(x)
lista.sort(key=len)



print('-----------')
for i in lista:
    print(i)
        

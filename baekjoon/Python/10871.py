n, x = map(int,input().split())
lista = ()
lista.append(input().split())
listb = ()
for i in lista:
    if int(i) < x:
        listb.append(i)


print(len(listb))



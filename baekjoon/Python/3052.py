lista = []
for i in range(10):
    a = int(input())
    x = a % 42
    lista.append(x)
lista2 = set(lista)
print(len(lista2))


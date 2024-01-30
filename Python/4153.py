while True:
    list1 = list(map(int,input().split()))
    lista = sorted(list1)
    if lista ==[0,0,0]:
        break
    else:
        if (lista[0] ** 2 + lista[1] ** 2) - lista[2] ** 2 == 0:
            print('right')
        else:
            print('wrong')

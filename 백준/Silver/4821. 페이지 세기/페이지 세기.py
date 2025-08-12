count = []
while True:
    try:
        n = int(input())
        if n == 0:
            break
        pages = input().split(',')
        result = []

        for i in pages:
            if i:
                if '-' in i:
                    n1, n2 = map(int, i.split('-'))
                    if n1 <= n2:
                        for ii in range(n1, n2 + 1):
                            if ii >= 1 and ii <= n:
                                result.append(ii)
                else:
                    if int(i) >= 1 and int(i) <= n:
                        result.append(int(i))
            
        count.append(len(set(result)))

    except (EOFError, ValueError):
        break

for i in count:
    print(i)
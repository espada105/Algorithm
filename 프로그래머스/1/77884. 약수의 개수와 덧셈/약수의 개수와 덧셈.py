def solution(left, right):
    list_sum = 0
    for i in range(left,right+1):
        listx = []
        for x in range(1,i+1):
            if i % x == 0:
                listx.append(x)
        if len(listx) % 2 == 0:
            list_sum += i
        else: 
            list_sum -= i
    return list_sum
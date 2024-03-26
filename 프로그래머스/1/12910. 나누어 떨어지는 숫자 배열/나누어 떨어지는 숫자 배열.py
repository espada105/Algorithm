def solution(arr, divisor):
    list_n = []
    for i in arr:
        if i % divisor == 0:
            list_n.append(i)
            
    if len(list_n) == 0:
        list_n.append(-1)    
    else:
        list_n = sorted(list_n)
        
    return list_n
            
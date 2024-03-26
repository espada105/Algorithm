def solution(num):
    t = 0
    if num == 1:
        return 0
    
    while 1:
        if (num % 2 == 0):
            num /= 2
        else:
            num = (num * 3) + 1
        t += 1
        
        if t == 500:
            return -1
        if num == 1:
            return t
    
        
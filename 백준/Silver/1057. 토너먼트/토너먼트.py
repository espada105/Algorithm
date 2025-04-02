def meet(n, jimin, hansu):
    round_num = 0
    
    while jimin != hansu:
        # 라운드 증가
        round_num += 1
        
        jimin = (jimin + 1) // 2
        hansu = (hansu + 1) // 2
        
        if jimin == hansu:
            return round_num

n, jimin, hansu = map(int, input().split())

print(meet(n, jimin, hansu))
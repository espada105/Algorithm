def solution(s):
    s_lower = s.lower()
    count_p = s_lower.count('p')
    count_y = s_lower.count('y')
    
    if count_p == count_y:
        return True
    else:
        return False

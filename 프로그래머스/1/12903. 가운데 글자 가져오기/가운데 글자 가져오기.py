def solution(s):
    
    if len(s) % 2 == 0:
        length = len(s)//2-1
        return s[length : length +2]
    else:
        length = len(s)//2
        return s[length]
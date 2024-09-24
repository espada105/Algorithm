def solution(s):
    
    s = s.lstrip('{').rstrip('}').split('},{')
    s = [set(map(int, x.split(','))) for x in s]
    
    s.sort(key=len)
    
    result = []
    for i in s:
        result.append((i - set(result)).pop())
    
    return result
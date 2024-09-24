def solution(s):
    
    s = s.lstrip('{').rstrip('}').split('},{')
    s = [set(map(int, x.split(','))) for x in s]
    
    s.sort(key=len)
    
    answer = []
    for group in s:
        answer.append((group - set(answer)).pop())
    
    return answer
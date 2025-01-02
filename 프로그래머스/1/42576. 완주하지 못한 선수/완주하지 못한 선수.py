from collections import Counter

def solution(participant, completion):
    
    Pc = Counter(participant)
    Cc = Counter(completion)
    
    result = Pc - Cc
    
    return list(result.keys())[0]

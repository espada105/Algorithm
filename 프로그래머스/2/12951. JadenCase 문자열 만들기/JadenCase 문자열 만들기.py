def solution(s):
    
    word = s.split(' ')
    
    for i in range(len(word)):
        word[i] = word[i].capitalize()
        
    return ' '.join(word)
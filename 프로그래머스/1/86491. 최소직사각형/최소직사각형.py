def solution(sizes):
    max_1 = 0
    max_2 = 0
    
    for i in range(len(sizes)):
        sizes[i] = sorted(sizes[i])
        if sizes[i][0] > max_1:
            max_1 = sizes[i][0]
        if sizes[i][1] > max_2:
            max_2 = sizes[i][1]
            
    return max_1 * max_2
            
            
        
                
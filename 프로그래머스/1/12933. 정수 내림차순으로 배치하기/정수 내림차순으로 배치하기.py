def solution(n):
    list_n = [int(i) for i in str(n)]
    new_list_n = sorted(list_n,reverse = True)
    merged_n = int(''.join(map(str, new_list_n)))  
    return(merged_n)
    
    
def solution(n):
    num = n -1
    list_num = [i for i in range(2,num+1) if num % i == 0 ]
    min_num = min(list_num)
    return min_num
import math
def solution(n):
    sqrt_n = int(math.sqrt(n))
    if n>0:
        if sqrt_n * sqrt_n != n:
            return -1
        else:
            answer = (sqrt_n + 1) * (sqrt_n + 1)
            return answer
    else:
        return -1
            
    
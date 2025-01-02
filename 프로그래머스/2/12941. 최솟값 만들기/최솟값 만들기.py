def solution(A,B):
    A = sorted(A)
    B = sorted(B)
    answer = 0
    
    for i in range(len(A)):
        answer += A[i] * B[-i-1]
        
    return answer
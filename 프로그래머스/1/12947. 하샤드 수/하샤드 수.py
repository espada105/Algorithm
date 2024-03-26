def solution(x):
    sum = 0
    answer = False
    listnum = [int(i) for i in str(x)]
    for i in range(len(listnum)):
        sum += listnum[i]
    if (x%sum) == 0:
        answer = True
    return answer
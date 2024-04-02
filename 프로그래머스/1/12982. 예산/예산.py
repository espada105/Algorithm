def solution(d, budget):
    newlist = sorted(d)
    count = 0
    for i in newlist:
        budget -= i

        if budget < 0:
            return count
        count += 1
            
    return count
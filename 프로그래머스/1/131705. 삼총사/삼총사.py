def solution(number):
    three = 0
    for i in range(len(number)):        
        for x in range(i+1,len(number)):
            for y in range(x+1,len(number)):
                if number[i]+number[x]+number[y] == 0:
                    three += 1
    return three
            
        
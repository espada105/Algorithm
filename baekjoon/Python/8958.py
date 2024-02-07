a= int(input())

for i in range(a):
    listx = list(input())
    count = 0
    score = 0
    for x in listx:
        if x =='O':
            count +=1
            score += count
        else:
            count = 0
    print(score)
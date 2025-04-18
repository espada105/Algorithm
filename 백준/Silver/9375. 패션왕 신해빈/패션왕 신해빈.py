T = int(input())

for _ in range(T):
    n = int(input())
    clothes = {}
    
    for _ in range(n):
        name, category = input().split()
        if category in clothes:
            clothes[category].append(name)
        else:
            clothes[category] = [name]
    
    counts = [len(items) for items in clothes.values()]
    
    answer = 1
    for count in counts:
        answer *= (count + 1)
    
    print(answer - 1)
def min_bags(N):
    five = N // 5
    
    for five_bags in range(five, -1, -1):
        remaining = N - (five_bags * 5)
        
        if remaining % 3 == 0:
            three = remaining // 3
            return five_bags + three
    
    return -1

N = int(input())
print(min_bags(N))
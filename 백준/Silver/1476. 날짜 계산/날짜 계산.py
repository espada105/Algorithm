E, S, M = map(int, input().split())

year = E 

while True:
    s = (year - 1) % 28 + 1
    m = (year - 1) % 19 + 1
    
    if s == S and m == M:
        print(year)
        break
    
    year += 15
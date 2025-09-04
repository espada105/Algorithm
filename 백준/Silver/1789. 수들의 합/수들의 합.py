S = int(input())

current_sum = 0  
count = 0        
i = 1            

while True:
    current_sum += i
    if current_sum > S:
        break
    count += 1
    i += 1

print(count)
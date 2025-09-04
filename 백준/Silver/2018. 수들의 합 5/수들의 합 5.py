N = int(input())

count = 0
current_sum = 0
start = 1
end = 1

while end <= N:
    if current_sum < N:
        current_sum += end
        end += 1
    elif current_sum > N:
        current_sum -= start
        start += 1
    else:
        count += 1
        current_sum += end
        end += 1
        
if N == 1:
    print(1)
else:
    print(count + 1)
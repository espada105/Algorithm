n = int(input())
count = 0

for i in range(n):
    group_str = input()
    check = []
    is_group_word = True
    
    for j in range(len(group_str)):
        if group_str[j] not in check:
            check.append(group_str[j])
        else:
            if group_str[j] != check[-1]:
                is_group_word = False
                break
    
    if is_group_word:
        count += 1

print(count)
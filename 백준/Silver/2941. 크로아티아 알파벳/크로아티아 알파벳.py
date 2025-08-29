word = input()
count = 0
i = 0

while i < len(word):
    if i <= len(word) - 3 and word[i:i+3] == 'dz=':
        count += 1
        i += 3
    elif i <= len(word) - 2:
        if word[i:i+2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
            count += 1
            i += 2
        else:
            count += 1
            i += 1
    else:
        count += 1
        i += 1

print(count)

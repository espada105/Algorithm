x, y = input().split()

rev_x = int(x[::-1])
rev_y = int(y[::-1])

sum_rev = rev_x + rev_y

result = int(str(sum_rev)[::-1])

print(result)
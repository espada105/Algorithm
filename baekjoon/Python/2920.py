n = list(map(int, input().split()))
sorted_n = sorted(n)

if n == sorted_n:
    print('ascending')
elif n == sorted_n[::-1]:
    print('descending')
else:
    print('mixed')

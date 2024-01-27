n = list(map(int, input().split()))  # Convert input to a list of integers
sorted_n = sorted(n)  # Create a sorted version of the list

if n == sorted_n:
    print('ascending')
elif n == sorted_n[::-1]:
    print('descending')
else:
    print('mixed')

n = 1260
money = [500,100,50,10]
count = 0

for i in money:
    count += n // i
    n = n % i

print(count)

all_num = set(range(1,10001))
generate_num = set()


for i in range(1, 10001):
    for j in str(i):
        i = i + int(j)
    generate_num.add(i)

result = sorted(all_num - generate_num)

for i in result:
    print(i)
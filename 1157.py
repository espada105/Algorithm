mention = input().upper()
mention_list = list(set(mention))

cnt = []
for i in mention_list:
    count = mention.count
    cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(mention_list[(cnt.index(max(cnt)))])
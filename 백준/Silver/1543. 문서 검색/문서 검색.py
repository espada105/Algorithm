document = input()
keyword = input()

count = 0
i = 0

while i <= len(document) - len(keyword):
    if document[i:i+len(keyword)] == keyword:
        count += 1
        i += len(keyword)  
    else:
        i += 1 

print(count)
num = int(input())
line = 0

while num > line:
    num -= line
    line += 1

if(line % 2 == 0):
    print(str(num) + "/" + str(line - num + 1))
else:
    print(str(line - num + 1) + "/" + str(num) )
x,y,w,h = map(int,input().split())

# if(abs(x-w)>abs(y-h)):
#     a = h-y
#     b = 0-y
#     if(abs(h-y)>abs(0-y)):
#         print(abs(0-y))
#     else:
#         print(abs(h-y))
# else:
#     a = w-x
#     b = 0-x
#     if(abs(w-x)>abs(0-x)):
#         print(abs(0-x))
#     else:
#         print(abs(w-x))

a = w - x
b = x - 0
c = h - y
d = y - 0

num = [a,b,c,d]
print(min(num))
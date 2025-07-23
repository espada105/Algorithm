from datetime import *
n = list(map(int,input().split()))
day = list(map(int,input().split()))

if n[0] + 1000 < day[0]:
    print('gg')
elif n[0] + 1000 == day[0] and (n[1], n[2]) <= (day[1], day[2]):
    print('gg')
else:
    n = date(*n)
    day = date(*day)
    print('D-' + str(day.toordinal()- n.toordinal()))
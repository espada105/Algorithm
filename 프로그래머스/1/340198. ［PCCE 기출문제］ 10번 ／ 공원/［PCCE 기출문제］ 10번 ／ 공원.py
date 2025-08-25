def can_place(park, y, x, size):
    h, w = len(park), len(park[0])
    if y + size > h or x + size > w:
        return False
    for yy in range(y, y + size):
        for xx in range(x, x + size):
            if park[yy][xx] != '-1':
                return False
    return True

def solution(mats, park):
    mats = sorted(map(int, mats), reverse=True)
    best = -1
    for y in range(len(park)):
        for x in range(len(park[0])):
            if park[y][x] == '-1':
                for size in mats:
                    if can_place(park, y, x, size):
                        best = max(best, size)
                        break
    return best
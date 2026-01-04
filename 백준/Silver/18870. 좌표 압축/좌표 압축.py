import sys

input = sys.stdin.readline

n = int(input())
coords = list(map(int, input().split()))

sorted_coords = sorted(list(set(coords)))

coord_dict = {val: i for i, val in enumerate(sorted_coords)}

for x in coords:
    print(coord_dict[x], end=' ')
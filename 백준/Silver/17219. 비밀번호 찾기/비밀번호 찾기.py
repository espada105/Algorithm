import sys

n, m = map(int, input().split())

web_pw = {}

for _ in range(n):
    site, password = sys.stdin.readline().strip().split()
    web_pw[site] = password

for _ in range(m):
    site = sys.stdin.readline().strip()
    print(web_pw[site])
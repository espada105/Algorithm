from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0
for comb in combinations(cards, 3):
    card_sum = sum(comb)
    if card_sum <= m:
        max_sum = max(max_sum, card_sum)

print(max_sum)

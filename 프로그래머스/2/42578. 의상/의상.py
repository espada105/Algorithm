from collections import Counter

def solution(clothes):
    clothes_counter = Counter([category for _ , category in clothes])
    
    combinations = 1
    for count in clothes_counter.values():
        combinations *= (count + 1)
    
    return combinations - 1

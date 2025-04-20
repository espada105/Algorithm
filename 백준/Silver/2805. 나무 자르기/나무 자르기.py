def get_wood_amount(trees, height):
    return sum(max(0, tree - height) for tree in trees)

def find_max_height(trees, target_wood):
    left = 0
    right = max(trees)
    
    result = 0
    while left <= right:
        mid = (left + right) // 2
        wood_amount = get_wood_amount(trees, mid)
        
        if wood_amount >= target_wood:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return result

n, m = map(int, input().split())
trees = list(map(int, input().split()))

print(find_max_height(trees, m))
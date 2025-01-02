def solution(nums):
    take = int(len(nums)/2)
    lenP = len(set(nums))
    if take < lenP:
        return take
    else:
        return lenP
def solution(arr):
    new_list = []
    for i in range(len(arr)):
        if i == len(arr) - 1 or arr[i] != arr[i + 1]:
            new_list.append(arr[i])
    return new_list

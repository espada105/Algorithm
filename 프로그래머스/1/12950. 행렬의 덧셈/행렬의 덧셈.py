def solution(arr1, arr2):
    for i in range(len(arr1)):
        for x in range(len(arr1[i])):
            arr1[i][x] += arr2[i][x]
    return arr1
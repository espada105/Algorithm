graph = [[999],[4,5],[999],[4,5],[2,3],[8],[2,3],[8],[6,7]]
result = []

while True:
    array = list(map(int, input()))
    
    if array[0] == 0:
        break

    count = len(array)

    if array[0] == 1 and array[-1] == 2:
        for i in range(count-1):
            if array[i+1] not in graph[array[i]]:
                result.append('NOT')
                break
            if i == (count -2):
                if array.count(1) == array.count(2) and array.count(5) == array.count(6):
                    result.append('VALID')
                else:
                    result.append('NOT')
            
    else:
        result.append('NOT')



for i in range(len(result)):
    print(f'{i+1}. {result[i]}')

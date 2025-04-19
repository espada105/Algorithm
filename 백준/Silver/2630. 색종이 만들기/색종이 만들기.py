N = int(input())
count1 = 0
count2 = 0
arrays = [list(map(int, input().split())) for _ in range(N)]

def one_quarter(papers, size):
    global count1, count2
    
    all_ones = all(papers[i][j] == 1 for i in range(size) for j in range(size))
    all_zeros = all(papers[i][j] == 0 for i in range(size) for j in range(size))
    
    if all_ones:
        count1 += 1
        return
    if all_zeros:
        count2 += 1
        return
    
    half = size // 2
    
    newArray1 = [papers[i][:half] for i in range(half)]  
    newArray2 = [papers[i][half:] for i in range(half)]  
    newArray3 = [papers[i][:half] for i in range(half, size)]  
    newArray4 = [papers[i][half:] for i in range(half, size)]  
    
    one_quarter(newArray1, half)
    one_quarter(newArray2, half)
    one_quarter(newArray3, half)
    one_quarter(newArray4, half)

one_quarter(arrays, N)
print(count2)  
print(count1)  
def solution(wallet, bill):
    count = 0
    
    while True:
        if (wallet[0] >= bill[0] and wallet[1] >= bill[1]) or (wallet[0] >= bill[1] and wallet[1] >= bill[0]):
            return count
            break
        index = bill.index(max(bill)) 
        bill[index] = max(bill) // 2
        count += 1
        

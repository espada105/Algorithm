def solution(friends, gifts):
    gift_scores = {}
    for friend in friends:
        gift_scores[friend] = 0
    
    for gift in gifts:
        giver, receiver = gift.split()
        gift_scores[giver] += 1
        gift_scores[receiver] -= 1

    gift_matrix = {}
    for friend in friends:
        gift_matrix[friend] = {}
        for other in friends:
            if friend != other:
                gift_matrix[friend][other] = 0
    
    for gift in gifts:
        giver, receiver = gift.split()
        gift_matrix[giver][receiver] += 1
    
    next_month_gifts = {}
    for friend in friends:
        next_month_gifts[friend] = 0
    
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            friend1, friend2 = friends[i], friends[j]
            
            gift1_to_2 = gift_matrix[friend1][friend2]
            gift2_to_1 = gift_matrix[friend2][friend1]
            
            if gift1_to_2 > gift2_to_1:
                next_month_gifts[friend1] += 1
            elif gift2_to_1 > gift1_to_2:
                next_month_gifts[friend2] += 1
            else:
                if gift_scores[friend1] > gift_scores[friend2]:
                    next_month_gifts[friend1] += 1
                elif gift_scores[friend2] > gift_scores[friend1]:
                    next_month_gifts[friend2] += 1

    return max(next_month_gifts.values())
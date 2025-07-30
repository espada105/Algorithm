group_num = 1

while True:
    n = int(input())
    if n == 0:
        break
    
    if group_num > 1:
        print()
    
    print(f"Group {group_num}")
    
    people = []
    
    for i in range(n):
        line = input().split()
        name = line[0]
        messages = line[1:]
        people.append([name, messages])
    
    nasty_found = False
    
    for i in range(n):
        target_name = people[i][0]
        messages = people[i][1]
        
        for j in range(len(messages)):
            if messages[j] == 'N':
                writer_index = (i - j - 1) % n
                writer_name = people[writer_index][0]
                
                print(f"{writer_name} was nasty about {target_name}")
                nasty_found = True
    
    if not nasty_found:
        print("Nobody was nasty")
    
    group_num += 1
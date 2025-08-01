n = int(input())
students = []

for i in range(n):
    grades = list(map(int, input().split()))
    students.append(grades)

max_count = 0
temp_leader = 1

for i in range(n):
    same_class_students = set()
    
    for j in range(n):
        if i != j:
            for grade in range(5):
                if students[i][grade] == students[j][grade]:
                    same_class_students.add(j)
                    break
    
    count = len(same_class_students)
    
    if count > max_count:
        max_count = count
        temp_leader = i + 1

print(temp_leader)
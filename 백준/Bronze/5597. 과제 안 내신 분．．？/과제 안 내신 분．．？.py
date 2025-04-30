student = [int(i) for i in range(1,31)]
for i in range(28):
    n = int(input())
    student.remove(n)
print(student[0])
print(student[1])
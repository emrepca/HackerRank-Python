students = list()
n = 0
for _ in range(int(input())):
    n+=1
    name = input()
    score = float(input())
    alt_list = [name,score]
    students.append(alt_list)

students.sort(key = lambda x:x[1])

x = students[0][1]
print(f"x: {x}")
answer = []

for student in students:
    if student[1] > x:
        answer.append(student[0])
        if len(answer) == 2:
            break

print(answer)

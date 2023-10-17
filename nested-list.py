students = list()
n = 0
for _ in range(int(input())):
    n+=1
    name = input()
    score = float(input())
    alt_list = [name,score]
    students.append(alt_list)

students.sort(key = lambda x:x[1]) #sorted by note
filtered_students = []
min_score = students[0][1]
for student in students:
    if student[1] > min_score:
        filtered_students.append(student)

answer_list = []

for i in range(len(filtered_students)):
    if filtered_students[0][1] == filtered_students[i][1]:
        answer_list.append(filtered_students[i])
        
answer_list.sort(key = lambda x:x[0]) #sorted by alphabetical order
for answer in answer_list:
    print(answer[0])

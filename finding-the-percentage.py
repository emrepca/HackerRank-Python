if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    answer = 0
    if query_name in student_marks:
        for value in student_marks[query_name]:
            answer += value

    average = answer/3
    formatted_average = "{:.2f}".format(average)
    print(formatted_average)
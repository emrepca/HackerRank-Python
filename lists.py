N = int(input())
answer = []
for i in range(N):
    lists = list(input())
for i in lists:
    if lists[0] == "append":
        n_split = lists.split()
        answer.append(n_split[0])


    if "insert" in lists:
        n_split = lists.split()
        answer.insert(n_split[0],n_split[1])
    if "print" in lists:
        print(answer)
    if "remove" in lists:
        answer.remove()
    if "append" in lists:
        n_split = lists.split()
        answer.append(n_split[1])
    if "sort" in lists:
        answer.sort()
    if "pop" in lists:
        answer.pop()
    if "reverse" in lists:
        answer.pop()
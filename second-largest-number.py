n = int(input())
arr = map(int, input().split())
arr_list = list(arr)
x = max(arr_list)
y = min(arr_list)

for i in range(0, n):
    if arr_list[i] < x and arr_list[i] > y:
        y = arr_list[i]

print(y)


#veya bu şekilde de yapabiliriz
"""n = int(input())
arr = map(int, input().split())
arr_list = list(arr)
arr_list.sort()
x = max(arr_list)

for i in range(0, n):
    if arr_list[i] < x:
        y = arr_list[i]

print(y)"""
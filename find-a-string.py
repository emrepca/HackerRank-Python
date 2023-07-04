def count_substring(string, sub_string):
    answer = 0
    sub_string_lenght = len(sub_string)
    for i in range(len(string)):
        if string[i:i+sub_string_lenght] == sub_string:
            answer+=1
    return answer



string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)
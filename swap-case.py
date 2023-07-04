def swap_case(s):
    new_string = ""
    for n in s:
        if n.isupper():
            new_string += n.lower()
        else:
            new_string += n.upper()
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
def print_formatted(number):
    decimal_list = []
    for numbers in range(1,number+1):
        decimal = ""
        decimal = str(int(numbers)%2)+decimal
        numbers=numbers // 2
        decimal_list.append(decimal)
    return decimal_list




if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
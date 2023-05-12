def solution(my_string, n):
    return ''.join([my_string[i] for i in range(len(my_string) - n, len(my_string))])
def solution(str_list):
    if len(str_list) > 1:
        for i in range(len(str_list)):
            if str_list[i] == 'l':
                return str_list[:i]
            elif str_list[i] == 'r':
                return str_list[i + 1:]
    else:
        return []
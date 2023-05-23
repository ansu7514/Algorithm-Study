def solution(my_string, queries):
    my_list = list(str(my_string))
    
    for start, end in queries:
        temp = my_list[start:end + 1][::-1]
        my_list = my_list[:start] + temp + my_list[end + 1:]
        
    return ''.join(my_list)
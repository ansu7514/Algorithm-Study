def solution(my_string):
    my_string = my_string.strip()
    answer = my_string.split(' ')
    
    return [s for s in answer if s != ""]
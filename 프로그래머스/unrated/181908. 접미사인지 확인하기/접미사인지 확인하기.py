def solution(my_string, is_suffix):
    answer = []
    
    start = 0
    for i in range(len(my_string)):
        answer.append(my_string[start:])
        start += 1
        
    return 1 if is_suffix in answer else 0
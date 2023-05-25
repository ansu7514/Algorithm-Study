def solution(my_string, is_prefix):
    answer = []
    
    end = 1
    for i in range(len(my_string)):
        answer.append(my_string[:end])
        end += 1
    
    return 1 if is_prefix in answer else 0
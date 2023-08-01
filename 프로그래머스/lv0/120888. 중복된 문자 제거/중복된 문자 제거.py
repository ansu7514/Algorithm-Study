def solution(my_string):
    strlist = list(my_string)
    
    answer = []
    for s in strlist:
        if s not in answer:
            answer.append(s)
    
    return ''.join(answer)
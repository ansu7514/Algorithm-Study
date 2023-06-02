def solution(my_string):
    answer = my_string
    dellist = ['a', 'e', 'i', 'o', 'u']
    
    for d in dellist:
        answer = answer.replace(d, '')
        
    return answer
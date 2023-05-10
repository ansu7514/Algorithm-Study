def solution(my_string, overwrite_string, s):
    strlist = list(my_string)
    
    answer = ''
    for i in range(0, len(strlist)):
        if i < s:
            answer += strlist[i]
            
    answer += overwrite_string
    
    for i in range(s + len(overwrite_string), len(strlist)):
        if i > s:
            answer += strlist[i]
            
    return answer
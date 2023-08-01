def solution(my_string, num1, num2):
    strlist = list(my_string)
    
    temp = strlist[num1]
    strlist[num1] = strlist[num2]
    strlist[num2] = temp
    
    return ''.join(strlist)
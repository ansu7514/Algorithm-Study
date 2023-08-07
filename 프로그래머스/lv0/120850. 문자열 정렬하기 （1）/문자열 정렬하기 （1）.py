def solution(my_string):
    strlist = list(my_string)
    
    return sorted([int(s) for s in strlist if s.isdecimal()])
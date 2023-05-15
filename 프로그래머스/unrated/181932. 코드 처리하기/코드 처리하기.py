def solution(code):
    mode = 0
    ret = ''
    
    temp = list(code)
    for i in range(0, len(code)):
        if temp[i] == '1':
            mode = 0 if mode else 1
            continue
            
        if (mode == 0 and i % 2 == 0) or (mode == 1 and i % 2 != 0):
            ret += str(temp[i])
            
    return ret if len(ret) != 0 else 'EMPTY'
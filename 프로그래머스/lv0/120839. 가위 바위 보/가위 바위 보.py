def solution(rsp):
    answer = ''
    rspList = list(rsp)
    
    for l in rspList:
        if l == '2':
            answer += '0'
        elif l == '0':
            answer += '5'
        else:
            answer += '2'
    
    return answer
def solution(s):
    check = {}
    
    for st in list(s):
        if st in check.keys():
            temp = check[st] + 1
            check[st] = temp
        else:
            check[st] = 1
    
    answer = ''
    for k in sorted(check):
        if check[k] == 1:
            answer += k
    
    return answer
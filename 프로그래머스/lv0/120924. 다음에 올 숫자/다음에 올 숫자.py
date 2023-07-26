def solution(common):
    cnt = 0
    
    if common[1] - common[0] == common[2] - common[1]:
        cnt = common[1] - common[0]
        return common[-1] + cnt
    else:
        cnt = common[1] // common[0]
        return common[-1] * cnt
def solution(array):
    check = {}
    
    for num in array:
        if num in list(check.keys()):
            check[num] += 1
        else:
            check[num] = 1

    maxCnt = 0
    for num in list(check.keys()):
        if maxCnt < check[num]:
            maxCnt = check[num]

    count = [v for v in list(check.values()) if maxCnt == v]

    if len(count) == 1:
        return [num for num in list(check.keys()) if check[num] == maxCnt].pop()
    else:
        return -1
        
def solution(my_string):
    arr = [0] * 52
    
    for s in my_string:
        curIdx = 0
        curAlpha = ord(s)
        
        if curAlpha >= 97:
            curIdx = curAlpha - 71
        else:
            curIdx = curAlpha - 65
        arr[curIdx] = arr[curIdx] if arr[curIdx] is not None else 0
        arr[curIdx] += 1

    return arr
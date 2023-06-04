def solution(myString, pat):
    result = []
    for i in range(len(myString)):
        curStr = myString[:i+1]
        if curStr.endswith(pat):
            result.append(curStr)

    result.sort(key=lambda x: len(x), reverse=True)
    return result[0]
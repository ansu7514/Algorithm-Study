def solution(num, k):
    numList = list(map(int, str(num)))
    
    for i in range(len(numList)):
        if numList[i] == k:
            return i + 1
    
    return -1
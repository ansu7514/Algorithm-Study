def solution(array, n):
    arrList = []
    
    for arr in array:
        arrList.append(abs(arr - n))
    
    answer = []
    for i in range(len(array)):
        if arrList[i] == min(arrList):
            answer.append(array[i])
            
    return min(answer)
def solution(order):
    numList = list(map(int, str(order)))
    
    answer = 0
    for num in numList:
        if num == 3 or num == 6 or num == 9:
            answer += 1
    
    return answer
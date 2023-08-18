def solution(hp):
    answer = hp // 5
    last = hp % 5
    
    if last != 0:
        answer += last // 3
        last = last % 3
    
    if last != 0:
        answer += last
    
    return answer
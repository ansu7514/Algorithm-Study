def solution(k, m, score):
    score.sort(reverse = True)
    answer = 0
    
    for i in range(0, len(score), m):
        temp = score[i:i + m]
        if len(temp) == m:
            answer += temp[-1] * m
            
    return answer
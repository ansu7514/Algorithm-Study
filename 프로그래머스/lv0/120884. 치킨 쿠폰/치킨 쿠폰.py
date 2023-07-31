def solution(chicken):
    answer = 0
    
    while chicken >= 10:
        quo = chicken // 10
        rem = chicken % 10
        
        answer += quo
        chicken = quo + rem

    return answer
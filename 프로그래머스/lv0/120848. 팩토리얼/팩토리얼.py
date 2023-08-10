def solution(n):
    answer = 1
    num = 1
    
    while num <= n:
        answer += 1
        num *= answer
            
    return answer - 1
def solution(n):
    answer = 0
    
    for i in range(n):
        temp = i + 1
        
        if n % temp == 0:
            answer += i + 1
    
    
    return answer
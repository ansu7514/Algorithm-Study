def solution(l, r):
    answer = []
    
    for i in range(l, r + 1):
        if i % 5 != 0:
            continue
        
        if not all(a == '5' or a == '0' for a in str(i)):
            continue
            
        answer.append(i)
    
    return answer if len(answer) else [-1]
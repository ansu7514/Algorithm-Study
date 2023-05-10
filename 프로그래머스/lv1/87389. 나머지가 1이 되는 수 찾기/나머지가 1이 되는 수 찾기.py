def solution(n):
    answer = 0
    x = 1
    
    while True:
        answer = n % x
        
        if answer == 1:
            break
        else:
            x += 1
    
    return x
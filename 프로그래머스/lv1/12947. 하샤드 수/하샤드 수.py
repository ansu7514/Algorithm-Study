def solution(x):
    answer = True
    
    numArr = list(str(x))
    
    sum = 0
    for num in numArr:
        sum += int(num)
        
    if x % sum != 0:
        answer = False
    
    return answer
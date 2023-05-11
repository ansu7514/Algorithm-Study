def solution(n):
    numLen = 0
    for num in range(1, n + 1):
        if n % num == 0:
            numLen += 1
    
    return numLen
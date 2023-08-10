def solution(n):
    num = 1
    
    while num * num < n:
        num += 1

    if num * num == n:
        return 1
    else:
        return 2
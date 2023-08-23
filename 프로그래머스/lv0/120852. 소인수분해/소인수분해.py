def solution(n):
    d = 2

    arr = []
    while d <= n:
        if n % d == 0:
            if d not in arr:
                arr.append(d)
            n = n / d
        else:
            d += 1
            
    return arr
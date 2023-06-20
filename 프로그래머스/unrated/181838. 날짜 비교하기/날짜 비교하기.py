def solution(date1, date2):
    y1, d1, m1 = date1
    y2, d2, m2 = date2
    
    if y1 < y2:
        return 1
    elif y2 < y1:
        return 0
    elif d1 < d2:
        return 1
    elif d2 < d1:
        return 0
    elif m1 < m2:
        return 1
    else:
        return 0
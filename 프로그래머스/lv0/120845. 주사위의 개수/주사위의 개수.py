def solution(box, n):
    w, h, d = box
    
    w = w // n
    h = h // n
    d = d // n
    
    return w * h * d
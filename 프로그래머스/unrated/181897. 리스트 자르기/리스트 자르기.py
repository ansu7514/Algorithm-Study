def solution(n, slicer, num_list):
    a, b, c = slicer
    
    if n == 1:
        return num_list[:b + 1] if b < len(num_list) else []
    elif n == 2:
        return num_list[a:] if a < len(num_list) else []
    elif n == 3:
        if a >= len(num_list) or b >= len(num_list):
            return []
        return num_list[a:b + 1]
    elif n == 4:
        if a >= len(num_list) or b >= len(num_list):
            return []
        return num_list[a:b + 1:c] if c != 0 else []
    else:
        return []
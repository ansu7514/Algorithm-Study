def solution(sides):
    max_side = max(sides)
    sides.remove(max_side)
    other_side = sum(sides)
    
    return 1 if max_side < other_side else 2
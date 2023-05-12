def solution(a, b):
    sum1 = int(str(a) + str(b))
    sum2 = int(str(b) + str(a))
    
    if sum1 > sum2 or sum1 == sum2:
        return sum1
    return sum2
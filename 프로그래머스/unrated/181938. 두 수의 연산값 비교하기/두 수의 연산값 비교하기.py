def solution(a, b):
    sum1 = int(str(a) + str(b))
    sum2 = 2 * a * b
    
    return max(sum1, sum2)
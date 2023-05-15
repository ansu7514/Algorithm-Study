def solution(a, b, c):
    answer = a + b + c
    
    sum1 = a ** 2 + b ** 2 + c ** 2
    sum2 = a ** 3 + b ** 3 + c ** 3
    
    if a != b and b != c and a != c:
        return answer
    elif a == b and b == c and a == c:
        return answer * sum1 * sum2
    else:
        return answer * sum1
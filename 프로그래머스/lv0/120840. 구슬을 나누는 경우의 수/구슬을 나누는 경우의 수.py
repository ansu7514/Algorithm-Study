def factory(num):
    answer = 1
    for i in range(1, num + 1):
        answer *= i

    return answer

def solution(balls, share):
    mo = factory(balls)
    de = factory(balls - share) * factory(share)
    
    return mo // de
    
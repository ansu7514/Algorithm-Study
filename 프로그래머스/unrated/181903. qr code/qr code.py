def solution(q, r, code):
    temp = list(code)
    answer = ''
    
    for i in range(len(temp)):
        if i % q == r:
            answer += temp[i]

    return answer
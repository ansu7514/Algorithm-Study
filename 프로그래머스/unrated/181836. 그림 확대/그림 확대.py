def solution(picture, k):
    answer = []
    
    for pic in picture:
        p = list(pic)
        temp = ''
        
        for i in range(len(p)):
            temp += p[i] * k
        
        for i in range(k):
            answer.append(temp)

    return answer
def solution(age):
    ageList = list(map(int, str(age)))
    answer = ''
    
    for a in ageList:
        if a == 0:
            answer += 'a'
        elif a == 1:
            answer += 'b'
        elif a == 2:
            answer += 'c'
        elif a == 3:
            answer += 'd'
        elif a == 4:
            answer += 'e'
        elif a == 5:
            answer += 'f'
        elif a == 6:
            answer += 'g'
        elif a == 7:
            answer += 'h'
        elif a == 8:
            answer += 'i'
        elif a == 9:
            answer += 'j'
    
    return answer
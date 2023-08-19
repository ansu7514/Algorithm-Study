def solution(emergency):
    temp = sorted(emergency, reverse=True)
    answer = [0 for e in emergency]
    
    num = 1
    for t in temp:
        for i in range(len(emergency)):
            if t == emergency[i]:
                answer[i] = num
                num += 1
    
    return answer
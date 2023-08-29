def solution(progresses, speeds):
    endDays = []
    
    for i in range(len(progresses)):
        endDay = (100 - progresses[i]) // speeds[i]
        
        if (100 - progresses[i]) % speeds[i] != 0:
            endDay += 1
        
        endDays.append(endDay)
        
    answer = [0]
    tempDay = endDays[0]
    for d in endDays:
        if tempDay >= d:
            answer[-1] += 1
        else:
            answer.append(1)
            tempDay = d
            
    return answer
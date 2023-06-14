def solution(strArr):
    answer = {};

    for s in strArr:
        if len(s) not in answer.keys():
            answer[len(s)] = 1
        else:
            answer[len(s)] += 1
            
    answer = list(answer.values())

    return max(answer)
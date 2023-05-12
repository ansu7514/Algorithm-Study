def solution(a, d, included):
    list = []
    for i in range(0, len(included)):
        if included[i]:
            list.append(i * d + a)
        
    return sum(list)
def solution(s):
    tupleList = s[1:len(s) - 1].split(',')
    tempList = []
    
    temp = []
    for t in tupleList:
        if '{' in t and '}' in t:
            tempList.append([int(t[1:len(t) - 1])])
        elif '{' in t and '}' not in t:
            temp.append(int(t[1:]))
        elif '{' not in t and '}' not in t:
            temp.append(int(t))
        elif '{' not in t and '}' in t:
            temp.append(int(t[:-1]))
            tempList.append(temp)
            temp = []
    
    tempList.sort(key=len)
    
    answer = []
    for temp in tempList:
        for t in temp:
            if t not in answer:
                answer.append(t)

    return answer
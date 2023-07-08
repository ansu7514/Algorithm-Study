def solution(clothes):
    cony = {}
    for name, types in clothes:
        if types not in list(cony.keys()):
            cony[types] = [name]
        else:
            tempList = cony[types]
            tempList.append(name)
            cony[types] = tempList

    numList = []
    for key in list(cony.keys()):
        numList.append(len(cony[key]))

    answer = 1
    for num in numList:
        answer *= (1 + num)

    return answer - 1
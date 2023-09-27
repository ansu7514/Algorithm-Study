def solution(n, computers):
    checkList = [0] * n
    answer = 0
    for idx in range(n):
        if checkList[idx] == 0:
            checkList[idx] = 1
            visitCheck(idx, checkList, computers)
            answer+=1
    return answer

def visitCheck(idx, checkList, computers):
    queue = []
    queue.append(idx)

    while len(queue) != 0:
        com = queue.pop(0)

        for i in range(len(computers)):
            if computers[com][i] == 1 and checkList[i] == 0:
                queue.append(i)
                checkList[i] = 2